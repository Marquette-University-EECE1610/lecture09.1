"""
controller.py

Controller for a phased MVC pygame example.

Responsibilities:
- capture events
- call model functions
- ask the view to draw each frame

The controller owns the game loop.

Note:
- The controller captures left/right key presses.
- The model decides what those key presses actually do.
"""

from __future__ import annotations

import pygame
# Pylint may flag pygame constants (e.g., QUIT, KEYDOWN, K_LEFT) as missing.
# They are dynamically exported by pygame at runtime.
# pylint: disable=no-member

import model
import view


def run_game(screen: pygame.Surface) -> None:
    """Run the main game loop."""
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    state = model.initial_state()

    while state["running"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state["running"] = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            state = model.move_paddle_left(state)
        if keys[pygame.K_RIGHT]:
            state = model.move_paddle_right(state)

        state = model.update(state)

        view.draw(screen, state, font)
        pygame.display.flip()
        clock.tick(60)
