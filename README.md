# MVC pygame example (phased)
This is a simple implementation of the Model-View-Controller (MVC) pattern using Pygame. The game is a basic paddle and ball game where the player controls a paddle to keep the ball from falling off the screen. The implementation is broken down into three phases to demonstrate the development process.

Phases:
1. Paddle movement with screen bounds
2. Ball falls with gravity
3. Collision detection + scoring + reset

Files:
- `model.py`
- `view.py`
- `controller.py`
- `main.py`

Create a virtual environment and activate it:
```bash
python -m venv .venv
.venv\Scripts\activate
```

Install required packages:
```bash
pip install -r requirements.txt 
```
Run with:
```bash
python main.py
```