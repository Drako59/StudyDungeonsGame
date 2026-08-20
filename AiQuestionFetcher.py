from google import genai

from google.genai import types
from pydantic import BaseModel

class QuestionModel(BaseModel):
    question: str
    answers: list[str]
    correct_answer: int


class QuestionClient:
    previousQuestions: list[str]
    level_diff: int = 0
    def __init__(self, API_KEY):
        self.__api_key = API_KEY
        try:
            self.client = genai.Client(api_key = self.__api_key)
        except:
            self.client = None
        self.previousQuestions = []
    def AddQuestionMemory(self, question) -> None:
        self.previousQuestions.append(question)


    def FetchQuestion(self, subjectName):
        try:
            response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=f"""
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
                    """,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=QuestionModel,
            )
            )

            question = QuestionModel.model_validate_json(response.text)
            self.level_diff += 1
            return question

        except:
            question: QuestionModel = QuestionModel()
            question.question = "What is your name?"
            question.answers  = ["Ofri", "Talya", "Itamar", "Eliran"]
            question.correct_answer = 0
            return  question

    