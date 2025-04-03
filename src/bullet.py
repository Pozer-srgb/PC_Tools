import pygame
from config import BULLET_SPEED, EXPLOSION_FRAMES

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Поверхность для пули (маленький красный прямоугольник)
        self.image = pygame.image.load("../assets/laser.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = BULLET_SPEED

    def update(self):
        """Двигаем пулю вверх и удаляем, если она ушла за экран."""
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = [pygame.image.load(frame).convert_alpha() for frame in EXPLOSION_FRAMES]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_speed = 0.1
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.current_frame +=1
            if self.current_frame >= len(self.frames):
                self.kill()
        else:
            base_size = self.frames[0].get_size()
            self.image = pygame.transform.scale(
                self.frames[self.current_frame],
                base_size
            )