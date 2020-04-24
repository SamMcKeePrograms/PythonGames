import pygame
import time

from OreganTrail.OreganTrail import Console
from OreganTrail.OreganTrail import Display
from OreganTrail.OreganTrail import Player

display_width = 800
display_height = 600

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Oregan Trail")
clock = pygame.time.Clock()

player = Player.Player(5, "Sam", 500)
display = Display.Display(gameDisplay)
console = Console.Console(gameDisplay)
print("Testeing Commiting")
#while not player.dead:
    #gameDisplay.fill((255, 255, 255))

    #for event in pygame.event.get():
        #if event.type == pygame.quit():
            #player.dead = True

    #pygame.display.update()
    #clock.tick(60)

pygame.quit()
exit()
quit()
