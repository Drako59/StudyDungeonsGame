import asyncio
import json
import sys

IN_BROWSER = sys.platform == "emscripten"

# google-genai is a native/desktop-only dependency - under pygbag we talk to the
# REST endpoint directly with the browser's own fetch().
if not IN_BROWSER:
    from google import genai
    from google.genai import types


GEMINI_MODEL = "gemini-3.5-flash-lite"
GEMINI_REST_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

# Plain OpenAPI schema instead of a pydantic model, so the same definition works
# for the SDK and for the raw REST call.
QUESTION_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "question": {"type": "STRING"},
        "answers": {"type": "ARRAY", "items": {"type": "STRING"}},
        "correct_answer": {"type": "INTEGER"},
    },
    "required": ["question", "answers", "correct_answer"],
}


class QuestionModel:
    question: str
    answers: list[str]
    correct_answer: int

    def __init__(self, question: str = "", answers: list[str] = None, correct_answer: int = 0) -> None:
        self.question = question
        self.answers = answers if answers is not None else []
        self.correct_answer = correct_answer

    @staticmethod
    def model_validate_json(raw: str) -> "QuestionModel":
        data = json.loads(raw)
        return QuestionModel(data["question"], list(data["answers"]), int(data["correct_answer"]))

    def __repr__(self) -> str:
        return f"QuestionModel(question={self.question!r}, answers={self.answers!r}, correct_answer={self.correct_answer})"


class QuestionClient:
    previousQuestions: list[str]
    level_diff: int = 0

    def __init__(self, API_KEY):
        self.__api_key = API_KEY
        self.client = None
        if not IN_BROWSER:
            try:
                self.client = genai.Client(api_key = self.__api_key)
            except:
                self.client = None
        self.previousQuestions = []

    def AddQuestionMemory(self, question) -> None:
        self.previousQuestions.append(question)


    def build_prompt(self, subjectName) -> str:
        return f"""
                Create one short multiple-choice {subjectName} question.

                Requirements:
                - Exactly 4 answers; exactly 1 correct.
                - correct_answer = correct answer index (0-3).
                - Difficulty: {self.level_diff}/30. Increase complexity significantly at higher levels.
                - Do NOT repeat or closely resemble previous questions.
                - Keep both the question and answers as short as possible.
                - Use varied topics appropriate to {subjectName}.
                - For math, progressively include advanced topics such as algebra, functions, geometry, trigonometry, derivatives, integrals, extrema, optimization, and areas.
                - At high levels, require multiple reasoning/calculation steps.
                - Wrong answers must be plausible, not obviously wrong.

                Previous questions to avoid:
                {self.previousQuestions}
                """


    async def FetchQuestion(self, subjectName):
        try:
            if IN_BROWSER:
                raw = await self.__fetch_browser(subjectName)
            else:
                # keeps the blocking SDK call off the game loop's thread
                raw = await asyncio.to_thread(self.__fetch_native, subjectName)

            question = QuestionModel.model_validate_json(raw)
            self.level_diff += 1
            return question

        except:
            question: QuestionModel = QuestionModel()
            question.question = "What is your name?"
            question.answers  = ["Ofri", "Talya", "Itamar", "Eliran"]
            question.correct_answer = 0
            return  question


    def __fetch_native(self, subjectName) -> str:
        response = self.client.models.generate_content(
        model=GEMINI_MODEL,
        contents=self.build_prompt(subjectName),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=QUESTION_SCHEMA,
        )
        )
        return response.text


    async def __fetch_browser(self, subjectName) -> str:
        from platform import window

        payload = {
            "contents": [{"parts": [{"text": self.build_prompt(subjectName)}]}],
            "generationConfig": {
                "responseMimeType": "application/json",
                "responseSchema": QUESTION_SCHEMA,
            },
        }
        # round-tripping through JSON.parse gives fetch() a real JS options object
        options = window.JSON.parse(json.dumps({
            "method": "POST",
            "headers": {
                "Content-Type": "application/json",
                "x-goog-api-key": self.__api_key,
            },
            "body": json.dumps(payload),
        }))

        response = await window.fetch(GEMINI_REST_URL, options)
        body = json.loads(await response.text())
        return body["candidates"][0]["content"]["parts"][0]["text"]
