import pygame
import random
import math
from config import WIDTH, HEIGHT, ENEMY_WAVE_AMPLITUDE, ENEMY_WAVE_SPEED

class Enemy(pygame.sprite.Sprite):
    """Информация о противнике."""
    def __init__(self, speed_range):
        super().__init__()
        self.image = pygame.image.load("../assets/enemy.png").convert_alpha()
        x = random.randint(50, WIDTH - 50)
        self.rect = self.image.get_rect(center=(x, -20))
        self.speed = random.randint(*speed_range)
        self.angle = 0

    def update(self):
        # Движение вниз
        self.rect.y += self.speed

        # Волнообразное смещение по X
        self.angle += ENEMY_WAVE_SPEED
        wave_offset = ENEMY_WAVE_AMPLITUDE * math.sin(self.angle)
        self.rect.x += wave_offset

        # Проверка выхода за экран
        if self.rect.top > HEIGHT:
            self.kill()