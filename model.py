"""
model.py

Model for a phased MVC pygame example.

This file is intentionally structured in phases so you can build the game in steps.

PHASE 1
- Move the paddle left/right when the controller calls the model.
- Keep the paddle on the screen.

PHASE 2
- Make the ball fall using gravity.
- Gravity should increase downward velocity over time.

PHASE 3
- Detect collisions between the ball and the paddle.
- On paddle catch:
    * add 3 to score
    * reset ball to a random x-position at the top
- On miss (ball hits bottom):
    * subtract 1 from score
    * reset ball to a random x-position at the top

Rules:
- Keep game rules in the model.
- The view should only draw.
- The controller should only handle events + loop coordination.
"""

from __future__ import annotations

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PADDLE_SPEED = 5
BALL_START_Y = 40
BALL_START_X = 320
GRAVITY = 0.35


def initial_state() -> dict:
    """Return the initial game state.

    State is stored in dictionaries on purpose for this example.
    """
    return {
        "ball": {
            "x": BALL_START_X,
            "y": BALL_START_Y,
            "radius": 15,
            "y_speed": 0.0,  # Phase 2: vertical speed
            "color": (220, 60, 60),
        },
        "paddle": {
            "x": 260,
            "y": 430,
            "width": 120,
            "height": 20,
            "color": (60, 160, 240),
        },
        "score": 0,
        "running": True,
        "background_color": (245, 245, 245),
    }


def clamp_paddle_x(x: int, paddle_width: int, screen_width: int) -> int:
    """Clamp the paddle so it stays fully on the screen."""
    if x < 0:
        return 0
    max_x = screen_width - paddle_width
    if x > max_x:
        return max_x
    return x


def move_paddle_left(state: dict) -> dict:
    """PHASE 1: move the paddle left.

    TODO:
    - Read the paddle x position from the state.
    - Subtract PADDLE_SPEED.
    - Clamp the result so the paddle does not go off the left side of the screen.
    - Store the updated x position back into the state.
    """
    return state


def move_paddle_right(state: dict) -> dict:
    """PHASE 1: move the paddle right.

    TODO:
    - Read the paddle x position from the state.
    - Add PADDLE_SPEED.
    - Clamp the result so the paddle does not go off the right side of the screen.
    - Store the updated x position back into the state.
    """
    return state


def reset_ball_to_top(state: dict) -> dict:
    """PHASE 3: reset the ball to a random x-position at the top.

    TODO:
    - Choose a random x value so the entire ball stays on the screen.
    - Set ball y back to BALL_START_Y.
    - Reset ball vertical velocity to 0.0.
    """
    return state


def ball_hits_paddle(state: dict) -> bool:
    """PHASE 3: return True if the ball overlaps the paddle.

    Suggested approach:
    - Treat the ball using its bounding box:
        left   = x - radius
        right  = x + radius
        top    = y - radius
        bottom = y + radius
    - Treat the paddle as a rectangle.
    - Use pygames collision detection functions.

    """
    return False


def ball_hits_bottom(state: dict) -> bool:
    """PHASE 3: return True if the ball has reached/passed the bottom of the screen."""
    return False


def apply_gravity(state: dict) -> dict:
    """PHASE 2: apply gravity to the ball.

    TODO:
    - Increase ball['y_speed'] by GRAVITY.
    - Then increase ball['y'] by ball['y_speed'].
    """
    return state


def update(state: dict) -> dict:
    """Advance the model by one frame.

    Build this in phases.

    PHASE 1
    - Nothing changes automatically yet.
    - Return the state unchanged.

    PHASE 2
    - Call apply_gravity(state).

    PHASE 3
    - After the ball moves:
        1. If ball_hits_paddle(state):
             - increase score by 3
             - reset ball to top
        2. elif ball_hits_bottom(state):
             - decrease score by 1
             - reset ball to top
    """
    return state
