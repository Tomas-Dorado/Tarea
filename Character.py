import pygame
from Entity import Entity
from Shot import Shot

class Character(Entity):
    def __init__(self, x, y, image=None, lives=3):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def shoot(self):
        return Shot(self.x + 25, self.y, -10 if isinstance(self, Player) else 10)

    def collide(self, other):
        return pygame.Rect(self.x, self.y, 50, 50).colliderect(
            pygame.Rect(other.x, other.y, 10, 10)
        )