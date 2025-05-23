import pygame
import random
from Player import Player
from Opponent import Opponent
from Boss import Boss


class Game:
    def __init__(self, SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600,  BLACK = (0, 0, 0), RED = (255, 0, 0), BLUE = (0, 0, 255)):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Juego de Disparos")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
        self.opponents = [Opponent(random.randint(0, SCREEN_WIDTH - 50), random.randint(-150, -50)) for _ in range(5)]
        self.shots = []
        self.score = 0
        self.boss = None  
        self.boss_defeated = False

    def start(self):
        while self.is_running:
            self.update()

    def update(self, SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600,WHITE=(255,255,255), BLACK = (0, 0, 0), RED = (255, 0, 0), BLUE = (0, 0, 255)):
        self.screen.fill(BLACK)
        keys = pygame.key.get_pressed()

        # Mueve al jugador
        self.player.move(keys)

        # Disparos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.shots.append(self.player.shoot())

        # Actualiza los disparos
        for shot in self.shots[:]:
            shot.move()
            if shot.y < 0 or shot.y > SCREEN_HEIGHT:
                self.shots.remove(shot)
            else:
                for opponent in self.opponents[:]:
                    if shot.hit_target(opponent):
                        self.shots.remove(shot)
                        opponent.is_star = True
                        self.opponents.remove(opponent)  # Elimina el oponente
                        self.score += 1

                # Revisa si el disparo golpea al jefe
                if self.boss and shot.hit_target(self.boss):
                    self.shots.remove(shot)
                    self.boss.lives -= 1
                    if self.boss.lives <= 0:
                        self.boss = None
                        self.boss_defeated = True
                        self.score += 10  # Bonus 

        # Actualiza los oponentes
        for opponent in self.opponents:
            opponent.move()
            if opponent.collide(self.player):
                self.player.lives -= 1
                opponent.y = -50
                opponent.x = random.randint(0, SCREEN_WIDTH - 50)
                if self.player.lives <= 0:
                    self.end_game()

        # CMira si el boss debe aparecer
        if not self.opponents and not self.boss and not self.boss_defeated:
            self.boss = Boss(SCREEN_WIDTH // 2, -100)

        # Actualiza al boss
        if self.boss:
            self.boss.move()
            if self.boss.collide(self.player):
                self.player.lives -= 1
                if self.player.lives <= 0:
                    self.end_game()

        # Dibuja todo
        self.player.draw(self.screen)
        for opponent in self.opponents:
            if opponent.is_star:
                pygame.draw.circle(self.screen, BLUE, (opponent.x + 25, opponent.y + 25), 25)
            else:
                opponent.draw(self.screen)
        for shot in self.shots:
            pygame.draw.rect(self.screen, RED, (shot.x, shot.y, 10, 10))

        # Dibuja al boss
        if self.boss:
            self.boss.draw(self.screen)

        # Mostrar el puntaje y las vidas
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        lives_text = font.render(f"Lives: {self.player.lives}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))

        pygame.display.flip()
        self.clock.tick(60)

    def end_game(self, SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600, WHITE=(255,255,255)):
        font = pygame.font.SysFont(None, 72)
        if self.boss_defeated and self.player.lives > 0:
            victory_text = font.render("Victory! You defeated the boss!", True, WHITE)
            self.screen.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, SCREEN_HEIGHT // 2))
        else:
            game_over_text = font.render("Game Over", True, WHITE)
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        self.is_running = False


