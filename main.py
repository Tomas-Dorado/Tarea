import pygame
from Game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.start()
    pygame.quit() 