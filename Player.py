import pygame
from Character import Character

class Player(Character):
    def __init__(self, x, y, image=None):
        super().__init__(x, y, image, lives=3)
        self.score = 0

    def move(self, keys, SCREEN_WIDTH=800, SCREEN_HEIGHT=600):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 5
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - 50:
            self.x += 5
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 5
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - 50:
            self.y += 5