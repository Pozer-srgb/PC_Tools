import pygame
from config import WIDTH, WHITE, RED

def draw_score(screen, score, font):
    """Отрисовывает счет в верхнем левом углу."""
    score_text = font.render(f"Счёт: {score}", True, WHITE )
    screen.blit(score_text, (10, 10))

def draw_lives(screen, lives, font):
    lives_text = font.render(f"HP: {lives}", True, RED)
    screen.blit(lives_text, (WIDTH - 120, 10))

def draw_level(screen, level, font):
    level_text = font.render(f"Уровень: {level}", True, WHITE)
    screen.blit(level_text, (WIDTH//2 - 50, 10))