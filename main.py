import pygame
from config import WIDTH, HEIGHT, FPS, BLACK, ENEMY_SPAWN_DELAY 
from player import Player
from bullet import Bullet
from enemy import Enemy
from ui import draw_score

pygame.init()

# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Группы спрайтов
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Создание игрока
player = Player()
all_sprites.add(player)

# Таймер спавна врагов
ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_EVENT, ENEMY_SPAWN_DELAY)

# Звук выстрела
shoot_sound = pygame.mixer.Sound("assets/shoot.wav")

# Переменные игры
running = True
score = 0

# Основной цикл игры
while running:
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Стрельба при нажатии пробела
                bullet = player.shoot(all_sprites)
                bullets.add(bullet)
                shoot_sound.play()
        elif event.type == ENEMY_EVENT:
            # Создаем нового врага
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

    # Обновление объектов
    keys = pygame.key.get_pressed()
    player.update(keys)
    bullets.update()
    enemies.update()

    # Проверка столкновений пуль с врагами
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        score += 10

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_score(screen, score, font)
    pygame.display.flip()

pygame.quit()