"""
main.py

Entry point for the phased MVC pygame ball-paddle-score example.
"""

from __future__ import annotations

import pygame
# Pylint may flag pygame constants (e.g., QUIT, KEYDOWN, K_LEFT) as missing.
# They are dynamically exported by pygame at runtime.
# pylint: disable=no-member

from controller import run_game


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("MVC Example - Ball, Paddle, Score (Phased)")

    run_game(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
