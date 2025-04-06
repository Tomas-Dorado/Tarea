import pygame

class Entity:
    def __init__(self, x, y, image=None):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        WHITE = (255, 255, 255)
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, WHITE, (self.x, self.y, 50, 50))