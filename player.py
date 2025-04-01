import pygame
from config import WIDTH, HEIGHT, PLAYER_SPEED
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    """Информация о корабле."""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT - 50))
        self.speed = PLAYER_SPEED
    
    def update(self, keys):
        """Двигаем корабль влево/вправо при нажатии клавиш."""
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
    
    def shoot(self, group):
        """Создаем пулю и добавляем ее в группу спрайтов."""
        bullet = Bullet(self.rect.centerx, self.rect.top)
        group.add(bullet)
        return bullet