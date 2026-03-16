"""
view.py

View for a very small MVC pygame example.

The view only draws:
- background
- ball
- paddle
- score

It does not decide movement, scoring, gravity, or collision.
"""

from __future__ import annotations

import pygame


def draw_ball(screen: pygame.Surface, ball: dict) -> None:
    """Draw the ball."""
    pygame.draw.circle(
        screen,
        ball["color"],
        (int(ball["x"]), int(ball["y"])),
        ball["radius"],
    )


def draw_paddle(screen: pygame.Surface, paddle: dict) -> None:
    """Draw the paddle."""
    rect = pygame.Rect(
        paddle["x"],
        paddle["y"],
        paddle["width"],
        paddle["height"],
    )
    pygame.draw.rect(screen, paddle["color"], rect)


def draw_score(screen: pygame.Surface, score: int, font: pygame.font.Font) -> None:
    """Draw the score in the upper-left corner."""
    text_surface = font.render(f"Score: {score}", True, (20, 20, 20))
    screen.blit(text_surface, (20, 15))


def draw(screen: pygame.Surface, state: dict, font: pygame.font.Font) -> None:
    """Draw the full frame from the current state."""
    screen.fill(state["background_color"])
    draw_ball(screen, state["ball"])
    draw_paddle(screen, state["paddle"])
    draw_score(screen, state["score"], font)
