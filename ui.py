import pygame
from config import (
    WIDTH, WHITE, RED, 
    PROGRESS_BAR_WIDTH, PROGRESS_BAR_HEIGHT, 
    PROGRESS_BAR_BG_COLOR, PROGRESS_BAR_FG_COLOR,
    PROGRESS_BAR_BORDER_COLOR, PROGRESS_BAR_BORDER_WIDTH
)

def draw_score(screen, score, font):
    """Отрисовывает счет в верхнем левом углу."""
    score_text = font.render(f"Счёт: {score}", True, WHITE )
    screen.blit(score_text, (10, 10))

def draw_lives(screen, lives, font):
    lives_text = font.render(f"HP: {lives}", True, RED)
    screen.blit(lives_text, (WIDTH - 120, 10))

def draw_level(screen, level, progress, font):
    # Текст уровня
    level_text = font.render(f"Уровень: {level}", True, WHITE)
    screen.blit(level_text, (WIDTH // 2 - 50, 10))

    # Координаты прогресс-бара
    bar_x = WIDTH // 2 - PROGRESS_BAR_WIDTH // 2
    bar_y = 50

    # Фон прогресс-бара
    pygame.draw.rect(screen, PROGRESS_BAR_BG_COLOR, (bar_x, bar_y, PROGRESS_BAR_WIDTH, PROGRESS_BAR_HEIGHT))

    # Заполненная часть
    filled_width = PROGRESS_BAR_WIDTH * progress
    pygame.draw.rect(screen, PROGRESS_BAR_FG_COLOR, (bar_x, bar_y, filled_width, PROGRESS_BAR_HEIGHT))

    # Рамка
    pygame.draw.rect(screen, PROGRESS_BAR_BORDER_COLOR, (bar_x, bar_y, PROGRESS_BAR_WIDTH, PROGRESS_BAR_HEIGHT), PROGRESS_BAR_BORDER_WIDTH)

    # Текст с процентами
    percent = int(progress * 100)
    percent_text = font.render(f"{percent}%", True, WHITE)
    text_rect = percent_text.get_rect(center=(bar_x + PROGRESS_BAR_WIDTH // 2, bar_y + PROGRESS_BAR_HEIGHT // 2))
    screen.blit(percent_text, text_rect)