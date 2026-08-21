import asyncio

from AiQuestionFetcher import QuestionModel,QuestionClient

from env import API_KEY



async def main():

    client: QuestionClient = QuestionClient(API_KEY=API_KEY)

    model: QuestionModel = await client.FetchQuestion("History")

    print(model)

if __name__ == '__main__':
    asyncio.run(main())