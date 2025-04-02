import pygame
from config import BULLET_SPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Поверхность для пули (маленький красный прямоугольник)
        self.image = pygame.image.load("assets/laser.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = BULLET_SPEED

    def update(self):
        """Двигаем пулю вверх и удаляем, если она ушла за экран."""
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()