import turtle

def kochCurve(t, length, depth):
    colors = ['cyan', 'magenta', 'light blue', 'purple', 'lavender', 'sky blue']
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        t.pencolor(colors[depth % len(colors)])
        kochCurve(t, length, depth - 1)
        t.left(60)
        kochCurve(t, length, depth - 1)
        t.right(120)
        kochCurve(t, length, depth - 1)
        t.left(60)
        kochCurve(t, length, depth - 1)

def kochSnowflake(t, length, depth):
    for _ in range(3):
        kochCurve(t, length, depth)
        t.right(120)

def main():
    t = turtle.Turtle()
    t.speed(0)  # Set turtle speed to max
    t.width(2)  # Make lines a bit thicker for visibility

    screen = turtle.Screen()
    screen.bgcolor("light yellow")

    length = 300  # Length of each side of the initial triangle
    depth = 4     # Depth of recursion

    # Position the turtle to start in the center of the screen
    t.penup()
    t.goto(-length / 2, length / 2.5)
    t.pendown()

    # Draw the Koch snowflake
    kochSnowflake(t, length, depth)

    screen.exitonclick()

main()

