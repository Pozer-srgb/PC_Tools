import pygame
from config import WIDTH, HEIGHT, FPS, BLACK, WHITE, PLAYER_LIVES, MUSIC_PATH, SOUND_SHOOT
from player import Player
from bullet import Bullet, Explosion
from enemy import Enemy
from ui import draw_score, draw_lives, draw_level
from level import LevelManager

def init_game():
    """Инициализирует все игровые объекты и настройки"""
    pygame.init()
    pygame.mixer.init()

    # Система уровней
    level_manager = LevelManager()
    initial_level = level_manager.get_current_level_config()

        # Настройки первого уровня
    current_enemy_speed = initial_level['enemy_speed_range']
    current_spawn_delay = initial_level['spawn_delay']
    PLAYER_LIVES = initial_level['player_lives']

    # Окно
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # Звуки и музыка
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.play(-1)
    shoot_sound = pygame.mixer.Sound(SOUND_SHOOT)

    # Группы спрайтов
    game_objects = {
        'all_sprites': pygame.sprite.Group(),
        'bullets': pygame.sprite.Group(),
        'enemies': pygame.sprite.Group(),
        'explosions': pygame.sprite.Group()
    }

    # Создание игрока
    player = Player()
    game_objects['all_sprites'].add(player)

    # Таймер спавна врагов
    ENEMY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMY_EVENT, current_spawn_delay)

    # Переменные игры
    game_state = {
        'running': True,
        'paused': False,
        'score': 0,
        'lives': PLAYER_LIVES,
        'ENEMY_EVENT': ENEMY_EVENT,
        'level_manager': level_manager,
        'current_enemy_speed': initial_level['enemy_speed_range'],
        'current_spawn_delay': initial_level['spawn_delay']
    }

    return {
        'screen': screen,
        'clock': clock,
        'font': font,
        'shoot_sound': shoot_sound,
        'player': player,
        'game_objects': game_objects,
        'game_state': game_state
    }

init_data = init_game()

def handle_events(game_objects, game_state, shoot_sound, player):
    """Обрабатывает все события игры и изменяет состояние игры"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state['running'] = False
            return False
        
        # Стрельба при нажатии пробела
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = player.shoot(game_objects['all_sprites'])
                game_objects['bullets'].add(bullet)
                shoot_sound.play()
        
            # Пауза по ESC
            elif event.key == pygame.K_ESCAPE:
                 game_state['paused'] = not game_state['paused']

        # Создаем нового врага
        elif event.type == game_state['ENEMY_EVENT'] and not game_state['paused']:
            enemy = Enemy(game_state['current_enemy_speed'])
            game_objects['all_sprites'].add(enemy)
            game_objects['enemies'].add(enemy)
    return True

# Основной цикл игры
while init_data['game_state']['running']:

    screen = init_data['screen']
    clock = init_data['clock']
    font = init_data['font']
    shoot_sound = init_data['shoot_sound']
    player = init_data['player']
    game_objects = init_data['game_objects']
    game_state = init_data['game_state']

    clock.tick(FPS)

    # Проверка повышения уровня
    level_manager = game_state['level_manager']
    if level_manager.check_level_up(game_state['score']):
        new_level_config = level_manager.get_current_level_config()

        game_state['current_enemy_speed'] = new_level_config['enemy_speed_range']
        game_state['current_spawn_delay'] = new_level_config['spawn_delay']

        game_state['lives'] = new_level_config['player_lives']

        pygame.time.set_timer(game_state['ENEMY_EVENT'], game_state['current_spawn_delay'])

    # Обработка событий
    if not handle_events(game_objects, game_state, shoot_sound, player):
        break

    if not game_state['paused']:
        # Обновление объектов
        keys = pygame.key.get_pressed()
        player.update(keys)
        game_objects['bullets'].update()
        game_objects['enemies'].update()
        game_objects['explosions'].update()

    # Проверка столкновений пуль с врагами
    hits = pygame.sprite.groupcollide(game_objects['bullets'], game_objects['enemies'], True, True)
    for hit in hits:
        game_state['score'] += 10
        explosion = Explosion(hit.rect.centerx, hit.rect.centery)
        game_objects['all_sprites'].add(explosion)
        game_objects['explosions'].add(explosion)
    
    # Проверка столкновений игрока с врагами
    player_hits = pygame.sprite.spritecollide(player, game_objects['enemies'], True)
    if player_hits:
        game_state['lives'] -= 1
        if game_state['lives'] <= 0:
            game_state['running'] = False

    # Отрисовка
    screen.fill(BLACK)
    game_objects['all_sprites'].draw(screen)
    draw_score(screen, game_state['score'], font)
    draw_lives(screen, game_state['lives'], font)
    draw_level(screen, level_manager.current_level, font)

    if game_state['paused']:
        pause_text = font.render("ПАУЗА", True, WHITE)
        text_rect = pause_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(pause_text, text_rect)

    pygame.display.flip()

pygame.quit()