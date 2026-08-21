import asyncio
import pygame
from answer import Answer
from textBlock import TextBlock
from consts import *
from AiQuestionFetcher import QuestionModel, QuestionClient
from env import API_KEY
from dungeon_enum import Subject

class Enemy: 
    __x: int = 0 #raw x placment
    __y: int = 0 #raw y placment


    __question: TextBlock
    __answers: list[Answer]
    # __ix: int  = 0 #x placment by matrix index
    # __iy: int = 0 #y placment by matrix index

    __enemySizes: tuple[int] = (10,10)

    windowBackground: object

    def __init__(self,backgroundImage,enemyImage, bossImage ,x,y,enemySizes: tuple[int],screen,clock, question: str,answers: list[str], rightAnswer, client: QuestionClient, subject: Subject) -> None:
            self.__answers = []
            self.__enemySizes = enemySizes
            self.enemyImage = pygame.transform.scale(enemyImage, self.__enemySizes)

            # self.__iy = iy
            # self.__ix = ix

            self.__x = x
            self.__y = y


            self.__enemySize = enemySizes
            self.bossImage = pygame.transform.scale(bossImage, self.__enemySize)

            self.screen = screen
            self.clock = clock

            # self.load_answers(answers,rightAnswer)
            # self.load_question(question)
            self.windowBackground = pygame.transform.scale(backgroundImage, self.screen.get_size())
            self.subject = subject
            self.client = client


    async def FetchQuestion(self):
        model: QuestionModel = await self.client.FetchQuestion(self.subject.name)

        self.load_answers(model.answers, model.answers[model.correct_answer])
        self.load_question(model.question)  
        self.client.AddQuestionMemory(model.question)

    def show(self) -> None:
        self.screen.blit(self.enemyImage, (self.__x, self.__y))

    def show_boss(self) -> None:
        self.screen.blit(self.bossImage, (self.__x, self.__y))


    def load_answers(self, answers, right_answer) -> None:
        screen_size = self.screen.get_size() # (width: int, height: int)
        block_size = [x // 100 for x in screen_size]
        
        answer_backgroun = pygame.image.load(ANSWER_BACKGROUND).convert_alpha()
        pos_ls = [(block_size[0] * 15,block_size[1] * 40),(block_size[0] * 15, block_size[1] * 80),(block_size[0] * 55, block_size[1] * 40),(block_size[0] * 55, block_size[1] * 80)]
        i: int = 0
        for answer in answers:
            
            answer_obj = Answer(answer_backgroun,answer, answer == right_answer, pos_ls[i],(block_size[0] * 30, block_size[1] * 30),self.screen)
            self.__answers.append(answer_obj)
            i += 1

    def load_question(self, question: str):
        screen_size = self.screen.get_size() # (width: int, height: int)
        block_size = [x // 100 for x in screen_size]
        
        question_backgroun = pygame.image.load(ANSWER_BACKGROUND).convert_alpha()
        pos = (block_size[0] * 21,block_size[1] * 10)
            
        self.__question = TextBlock(question_backgroun,question, pos,(block_size[0] * 60, block_size[1] * 30),self.screen)


    async def ShowDialogQuestion(self) -> bool:
        await self.FetchQuestion()
        while True:
            self.screen.blit(self.windowBackground, (0,0))
            self.__question.show()
            for answer  in self.__answers:
                answer.show()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.event.clear()
                        return False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.event.clear()
                return False

            pos  = pygame.mouse.get_pos()

            for answer in self.__answers:
                if answer.check_click(pos):
                    return answer.isRightAnswer
            
            self.clock.tick(400)
            pygame.display.flip()
            await asyncio.sleep(0)
         
