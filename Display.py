from OreganTrail.OreganTrail.Player import Player
import pygame
class Display:
    black  = (0,0,0)
    white = (255,255,255)



    gameDispay = None

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

    def displayData(self):
        pass
        # smallText = pygame.font.Font('freesansbold.ttf', 30)
        # TextSurf, TextRect = text_object(text, smallText)