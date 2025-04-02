import pygame
from config import WIDTH, HEIGHT, FPS, BLACK, WHITE, ENEMY_SPAWN_DELAY, PLAYER_LIVES, MUSIC_PATH, SOUND_SHOOT
from player import Player
from bullet import Bullet
from enemy import Enemy
from ui import draw_score, draw_lives

pygame.init()
pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.play(-1)

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
shoot_sound = pygame.mixer.Sound(SOUND_SHOOT)

# Переменные игры
running = True
paused = False
score = 0
lives = PLAYER_LIVES

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
                # Пауза по ESC
            elif event.key == pygame.K_ESCAPE:
                paused = not paused
        elif event.type == ENEMY_EVENT and not paused:
            # Создаем нового врага
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

    if not paused:
        # Обновление объектов
        keys = pygame.key.get_pressed()
        player.update(keys)
        bullets.update()
        enemies.update()

    # Проверка столкновений пуль с врагами
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        score += 10
    
    # Проверка столкновений игрока с врагами
    player_hits = pygame.sprite.spritecollide(player, enemies, True)
    if player_hits:
        lives -= 1
        if lives <= 0:
            running = False

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_score(screen, score, font)
    draw_lives(screen, lives, font)

    if paused:
        pause_text = font.render("ПАУЗА", True, WHITE)
        text_rect = pause_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(pause_text, text_rect)

    pygame.display.flip()

pygame.quit()