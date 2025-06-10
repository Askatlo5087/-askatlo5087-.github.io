'''
Andrew Kriese
Project Variation #1 Refactored for Project 5

Improvements:
- Extracted composite drawing functions: draw_house, draw_sun, draw_cloud for modularity.
- Parameterized positions, sizes, and colors to improve reusability.
- Eliminated redundant drawing and positioning logic.
- Organized code into logical sections: utilities, primitives, composites, scene.
- Ensured roof sits flush on house body, windows centered vertically, and door at base.
'''

import turtle
import math

# ---------- Utility Functions ----------

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment - Refactored")
    return t, screen


def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# ---------- Primitive Shape Drawers ----------

def draw_rectangle(t, width, height, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_square(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

# ---------- Composite Drawing Functions ----------

def draw_sun(t, x, y, radius, color="yellow"):
    jump_to(t, x, y)
    draw_circle(t, radius, fill_color=color)


def draw_cloud(t, x, y, scale=1.0):
    for dx, dy in [(-30, 0), (0, 10), (30, 0)]:
        jump_to(t, x + dx * scale, y + dy * scale)
        draw_circle(t, 20 * scale, fill_color="white")


def draw_house(
    t,
    x,
    y,
    width=200,
    height=150,
    body_color="red",
    roof_color="brown",
    door_width=40,
    door_height=80,
    door_color="yellow",
    window_size=40,
    window_color="lightblue"
):
    # Body
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, width, height, fill_color=body_color)
    # Roof (flush)
    jump_to(t, x, y + height - 150)
    t.setheading(0)
    draw_triangle(t, width, fill_color=roof_color) 
    # Door at base
    door_x = x + (width - door_width) / 2
    door_y = y - 70
    jump_to(t, door_x, door_y)
    t.setheading(0)
    draw_rectangle(t, door_width, door_height, fill_color=door_color)
    # Windows centered
    win_y = y + (height - window_size) / 2 - 80
    left_win_x = x + width * 0.15
    right_win_x = x + width - width * 0.15 - window_size
    jump_to(t, left_win_x, win_y)
    t.setheading(0)
    draw_square(t, window_size, fill_color=window_color)
    jump_to(t, right_win_x, win_y)
    t.setheading(0)
    draw_square(t, window_size, fill_color=window_color)

# ---------- Main Scene Drawing ----------

def draw_scene(t):
    """Draw the refactored scene: original and enhanced version."""
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # Original scene (Project 4 reproduction) with body at y=-250
    draw_sun(t, 150, 200, 50)
    draw_cloud(t, -250, 180, scale=1.0)
    draw_cloud(t, -150, 220, scale=0.8)
    draw_house(t, -100, -250)

    # Enhanced scene: second house shifted down to match
    draw_house(
        t,
        x=150,
        y=-250,
        body_color="orange",
        roof_color="darkred",
        door_color="purple",
        window_color="white"
    )
    draw_cloud(t, 0, 180, scale=1.2)
    draw_cloud(t, 100, 200, scale=0.6)

    t.hideturtle()


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()
    main()
