from AiQuestionFetcher import QuestionModel,QuestionClient

from env import API_KEY



def main():

    client: QuestionClient = QuestionClient(API_KEY=API_KEY)

    model: QuestionModel = client.FetchQuestion("History")

    print(model)

if __name__ == '__main__':
    main()