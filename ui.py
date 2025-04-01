import pygame
from config import WHITE

def draw_score(screen, score, font):
    """Отрисовывает счет в верхнем левом углу."""
    score_text = font.render(f"Score: {score}", True, WHITE )
    screen.blit(score_text, (10, 10))