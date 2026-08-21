import os

# pip install -U google-genai
# genai/gtts are unavailable under pygbag and the code using them is commented
# out below - keep these imports off until the DvdPlayer class is revived.
# from google import genai
import pygame
# from gtts import gTTS
from consts import *
# client = genai.Client()


# class DvdPlayer:
#     def __init__(self, image, size, screen, type):
#         self.__image = pygame.transform.scale(image, size)
#         self.__screen = screen
#         self.__Type = type

#     def load_image(self, pos) -> None:
#         self.__screen.blit(self.__image, pos)

#     def get_summery(self,sub):
#         res = client.interactions.create(
#             model=MODEL_AI,
#             input=f"Write me a summery for the subject {sub}, in hebrew",
#         )
#         self.text_to_speech(res.output_text)
#     def text_to_speech(self,text) -> None:
#         obj = gTTS(text=text, lang=LANGUAGE, slow=False)
#         obj.save(f"summery{self.__Type}.mp3")

#     def start_mp3(self) -> None:
#         os.system(f"start summery{self.__Type}.mp3")

