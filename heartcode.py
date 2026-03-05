import turtle


def draw_curve(t, steps=200, angle=1, distance=1):
    """Draws a smooth curve."""
    for _ in range(steps):
        t.right(angle)
        t.forward(distance)


def draw_heart(t):
    t.color("red", "pink")
    t.begin_fill()

    t.left(140)
    t.forward(111.65)

    draw_curve(t)
    t.left(120)
    draw_curve(t)

    t.forward(111.65)
    t.end_fill()


def write_quote(t):
    t.penup()
    t.goto(0, -120)
    t.color("white")
    t.write(
        '"Love looks not with the eyes, but with the mind."\n– William Shakespeare',
        align="center",
        font=("Arial", 12, "italic")
    )
    t.pendown()


def main():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(3)

    draw_heart(t)
    write_quote(t)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()