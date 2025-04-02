import pygame
from config import WIDTH, HEIGHT, PLAYER_SPEED
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    """Информация о корабле."""
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT - 50))
        self.speed = PLAYER_SPEED
        self.angel = 0
    
    def update(self, keys):
        """Двигаем корабль влево/вправо при нажатии клавиш."""
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.angel = 0

        if keys[pygame.K_LEFT]:
            self.angel = 15
        if keys[pygame.K_RIGHT]:
            self.angel = -15

        self.image = pygame.transform.rotate(self.original_image, self.angel)
        self.rect = self.image.get_rect(center=self.rect.center)

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
    
    def shoot(self, group):
        """Создаем пулю и добавляем ее в группу спрайтов."""
        bullet = Bullet(self.rect.centerx, self.rect.top)
        group.add(bullet)
        return bullet