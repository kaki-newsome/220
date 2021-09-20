"""
Name: Kaki Newsome
File: lab4.py

This program uses Python's graphics library and shows what it can do.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""
import math
from math import sqrt
from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(75, 75))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of square

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()

        shape2 = shape.clone()
        shape2.draw(win)

        shape.move(dx, dy)

        p1 = shape.getP1()
        p2 = shape.getP2()

        shape = Rectangle(p1, p2)
        shape.setOutline("red")
        shape.setFill("red")

        shape.draw(win)

        if i == 4:
            end_text = Text(Point(200, 20), "Click again to exit")
            end_text.draw(win)
        else:
            pass

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    width = 500
    height = 500
    win = GraphWin("draw rectangle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "click two places in the window")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    rect = Rectangle(p1, p2)
    rect.setFill('red')
    rect.setOutline('black')
    rect.draw(win)

    x_per = p2.getX() - p1.getX()
    y_per = p2.getY() - p1.getY()
    per = Text(Point(250, 10), ("The perimeter of your rectangle is", abs(x_per * 2 + y_per * 2)))
    area = Text(Point(250, 25), ("The area of your rectangle is", abs(x_per * y_per)))

    end = Text(Point(250, 475), "Click to close")

    per.draw(win)
    area.draw(win)
    end.draw(win)

    win.getMouse()


def circle():
    width = 500
    height = 500
    win = GraphWin("circle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "click once for the center, second for the circumference")
    instructions.draw(win)

    center = win.getMouse()
    circum = win.getMouse()

    cen_x = center.getX()
    cen_y = center.getY()
    circ_x = circum.getX()
    circ_y = circum.getY()

    rad = sqrt((abs(circ_x - cen_x)) ** 2 + (abs(circ_y - cen_y)) ** 2)

    circle = Circle(center, rad)

    circle.draw(win)
    circle.setOutline('black')
    circle.setFill('blue')

    rad_text = Text(Point(250, 10), ("The radius of your circle is", round(rad, 2)))
    rad_text.draw(win)

    end = Text(Point(250, 475), "Click to close")
    end.draw(win)

    win.getMouse()


def pi2():
    n = eval(input("Enter the number of terms you want to sum: "))

    pi = 0
    acc = 1
    for i in range(n):
        num = 4
        den = i + acc
        frac = (num / den) * ((-1) ** i)
        pi = pi + frac

        acc += 1

    print("Pi is: ", pi)
    print(math.pi - pi)



def main():
    # squares()
    # rectangle()
    # circle()
    # pi2()


main()
