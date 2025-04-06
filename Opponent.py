import random
from Character import Character

class Opponent(Character):
    def __init__(self, x, y, image=None):
        super().__init__(x, y, image, lives=1)
        self.is_star = False

    def move(self, SCREEN_WIDTH=800, SCREEN_HEIGHT=600):
        self.y += 2
        if self.y > SCREEN_HEIGHT:
            self.y = -50
            self.x = random.randint(0, SCREEN_WIDTH - 50)
