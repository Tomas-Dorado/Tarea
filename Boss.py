from Opponent import Opponent
import random

class Boss(Opponent):
    def __init__(self, x, y, image=None):
        super().__init__(x, y, image)
        self.lives = 5  
        self.speed = 4  

    def move(self, SCREEN_WIDTH=800, SCREEN_HEIGHT=600):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = -50
            self.x = random.randint(0, SCREEN_WIDTH - 50)