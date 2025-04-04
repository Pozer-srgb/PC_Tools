# Настройки экрана
WIDTH = 800                                                                                                 # Ширина окна
HEIGHT = 600                                                                                                # Высота окна
FPS = 60                                                                                                    # Кадры в секунду

# Цвета
BLACK = (0, 0, 0)                                                                                           # Цвет для фона
WHITE = (255, 255, 255)                                                                                     # Цвет для текста
RED = (255, 0, 0)                                                                                           # Цвет счётчика жизней

# Настройки игрока
PLAYER_SPEED = 5                                                                                            # Скорость корабля
PLAYER_LIVES = 3                                                                                            # Кол-во жизней

# Настройки пуль
BULLET_SPEED = -10                                                                                          # Отрицательное значение — пуля летит вверх

# Настройки врагов
BASE_ENEMY_SPEED = 2                                                                                        # Базовая скорость врага
BASE_SPAWN_DELAY = 1000                                                                                     # Базовая скорость появления врага (В мс)

# Музыка и звуки
SOUND_SHOOT = "../assets/shoot.wav"                                                                         # Звук выстрела
MUSIC_PATH = "../assets/background_music.ogg"                                                               # Фоновая музыка

# Изображения
EXPLOSION_FRAMES = ["../assets/explosion_1.png", "../assets/explosion_2.png", "../assets/explosion_3.png"]  # Фрэймы взрыва

# Прогресс-бар
PROGRESS_BAR_WIDTH = 200                                                                                    # Ширина прогресс-бара
PROGRESS_BAR_HEIGHT = 20                                                                                    # Высота прогресс-бара
PROGRESS_BAR_BG_COLOR = (50, 50, 50)                                                                        # Цвет фона полосы
PROGRESS_BAR_FG_COLOR = (0, 255, 0)                                                                         # Цвет заполнения полосы
PROGRESS_BAR_BORDER_COLOR = (200, 200, 200)                                                                 # Цвет рамки
PROGRESS_BAR_BORDER_WIDTH = 2                                                                               # Толщина рамки
PROGRESS_ANIMATION_SPEED = 0.1                                                                              # Скорость анимации (0.1 = плавно)
