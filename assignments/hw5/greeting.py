"""
Name: Kaki Newsome
File: greeting.py

This program creates a greeting card for Valentine's Day!

Certification of Authenticity:
I certify this assignment is entirely my own.
"""

import time
from graphics import GraphWin, Circle, Polygon, Point, Line, Text


def main():
    length = 500
    height = 500
    win = GraphWin("Greeting card", height, length)
    win.setBackground('pink')

    top_heart = Circle(Point(length / 3, 120), 94)
    bottom_heart = Polygon(Point(length / 2, 400), Point(length / 3 - 90, 150),
    Point(2 * length / 3 + 90, 150))
    arrow = Line(Point(25, 420), Point(150, 320))
    arrow.setArrow('last')

    top_heart.setFill('red')
    top_heart.setOutline('red')
    bottom_heart.setFill('red')
    bottom_heart.setOutline('red')
    arrow.setWidth(2)

    top_heart2 = top_heart.clone()
    top_heart2.move(length / 3, 0)

    message = "Happy Valentine's Day!"
    msg_text = Text(Point(length / 2, 450), message)
    msg_text.setSize(25)
    msg_text.setTextColor('gray')

    top_heart.draw(win)
    bottom_heart.draw(win)
    arrow.draw(win)
    top_heart2.draw(win)
    msg_text.draw(win)

    for _ in range(300):
        arrow.move(1, -1)
        time.sleep(0.01)

    msg_text.undraw()

    ending = "Click anywhere to close"
    end_text = Text(Point(length / 2, 450), ending)
    end_text.setSize(25)
    end_text.setTextColor('gray')

    end_text.draw(win)

    win.getMouse()

if __name__ == '__main__':
    main()
