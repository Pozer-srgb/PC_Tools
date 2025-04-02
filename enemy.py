import pygame
import random
from config import WIDTH, HEIGHT, ENEMY_MIN_SPEED, ENEMY_MAX_SPEED

class Enemy(pygame.sprite.Sprite):
    """Информация о противнике."""
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        x = random.randint(50, WIDTH - 50)
        self.rect = self.image.get_rect(center=(x, -20))
        self.speed = random.randint(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)

    def update(self):
        """Двигаем врага вниз и удаляем, если он ушел за экран."""
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()