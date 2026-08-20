from google import genai

from google.genai import types
from pydantic import BaseModel

class QuestionModel(BaseModel):
    question: str
    answers: list[str]
    correct_answer: int


class QuestionClient:
    level_diff: int = 0
    def __init__(self, API_KEY):
        self.__api_key = API_KEY
        self.client = genai.Client(api_key = self.__api_key)

    def FetchQuestion(self, subjectName):

        response = self.client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"""
        Create one multiple-choice {subjectName} question.

        Requirements:
        - Exactly 4 possible answers.
        - Only one answer is correct.
        - correct_answer must be the INDEX of the correct answer (0-3).
        - Do not make the answer obvious.
        - Make the question level {self.level_diff} out of 50
        - Make the text short as possible
        """,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=QuestionModel,
        )
        )

        question = QuestionModel.model_validate_json(response.text)
        self.level_diff += 1
        return question
    