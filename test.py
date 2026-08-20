from AiQuestionFetcher import QuestionModel,QuestionClient

from env import API_KEY



client: QuestionClient = QuestionClient(API_KEY=API_KEY)

model: QuestionModel = client.FetchQuestion("History")

print(model)