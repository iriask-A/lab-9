# 🎮 pygame-projects

A collection of Python mini-games and apps built with [Pygame](https://www.pygame.org/).

---

## Projects

### 🚗 Racer
A top-down car dodging game. Steer your car left and right to avoid oncoming enemies, and collect coins to boost your score. The game gets faster over time — how long can you last?

**Features**
- 3 coin types worth different point values
- Enemy and coin speed increases every 3 seconds and every 10 coins collected
- Game over screen on collision

**How to run**
```bash
cd racer
python racer.py
```
> Requires images: `enemy.png`, `player.png`, `coin.png`, `road.png` inside an `images/` folder.

---

### 🐍 Snake
A classic Snake game with a twist — food comes in three colors, each worth different points, and disappears after 10 seconds if you don't collect it in time.

**Features**
- 3 food types (red = 1pt, yellow = 2pt, green = 3pt)
- Food disappears after 10 seconds
- Speed and level increase as your score grows

**How to run**
```bash
cd snake
python snake.py
```

---

### 🎨 Paint
A simple drawing app. Choose from multiple colors and shapes, draw freely, or erase.

**Features**
- Freehand drawing and eraser
- Shapes: rectangle, circle, square, right triangle, equilateral triangle
- Color palette with 4 colors

**How to run**
```bash
cd paint
python paint.py
```

---

## Requirements

- Python 3.x
- Pygame

Install Pygame with:
```bash
pip install pygame
```

---

## Controls

| Game | Controls |
|------|----------|
| Racer | ← → arrow keys to steer |
| Snake | ↑ ↓ ← → arrow keys |
| Paint | Mouse to draw, click toolbar to switch tools |
