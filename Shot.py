import pygame
from Entity import Entity

class Shot(Entity):
    def __init__(self, x, y, speed, image=None):
        super().__init__(x, y, image)
        self.speed = speed

    def move(self):
        self.y += self.speed

    def hit_target(self, target):
        return pygame.Rect(self.x, self.y, 10, 10).colliderect(
            pygame.Rect(target.x, target.y, 50, 50)
        )