"""
Name: Kaki Newsome
File: bumper.py

This program creates a visual of bumper cars colliding at random times.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""
import math
import time
import random
from graphics import Circle, GraphWin, Point


def getaddsidex(circle):
    centerpoint = circle.getCenter()
    center = centerpoint.getX()
    circleside = center + circle.getRadius()
    return circleside


def getminussidex(circle):
    centerpoint = circle.getCenter()
    center = centerpoint.getX()
    circleside = center - circle.getRadius()
    return circleside


def getaddsidey(circle):
    centerpoint = circle.getCenter()
    center = centerpoint.getY()
    circleside = center + circle.getRadius()
    return circleside


def getminussidey(circle):
    centerpoint = circle.getCenter()
    center = centerpoint.getY()
    circleside = center - circle.getRadius()
    return circleside


def hit_horizontal(circle1, win):
    circle1right = getaddsidex(circle1)
    circle1left = getminussidex(circle1)
    circlecent = circle1.getCenter()
    circlex = circlecent.getX()
    if circle1.radius >= win.getWidth():
        return True
    if circle1right >= win.getWidth():
        return True
    if circle1left <= 0:
        return True
    if circlex + circle1.getRadius() >= win.getWidth():
        return True
    if circlex - circle1.getRadius() <= 0:
        return True
    return False


def hit_vertical(circle1, win):
    circle1top = getminussidey(circle1)
    circle1bottom = getaddsidey(circle1)
    circlecent = circle1.getCenter()
    circley = circlecent.getY()
    if circle1top <= 0:
        return True
    if circle1bottom >= win.getHeight():
        return True
    if circley + circle1.getRadius() >= win.getHeight():
        return True
    if circley - circle1.getRadius() <= 0:
        return True

    return False


def did_collide(circle1, circle2):
    circle1cent = circle1.getCenter()
    circle2cent = circle2.getCenter()

    dist = math.sqrt((circle1cent.getX() - circle2cent.getX()) ** 2 + \
                     (circle1cent.getY() - circle2cent.getY()) ** 2)
    circle1rad = circle1.getRadius()
    circle2rad = circle2.getRadius()

    if circle1rad + circle2rad >= dist:
        return True
    return False


def get_random(move_amnt):
    num = random.randint(-1 * move_amnt, move_amnt)
    return num


def cent_dist(circle1, circle2):
    circle1cent, circle2cent = circle1.getCenter(), circle2.getCenter()
    circle1x, circle2x = circle1cent.getX(), circle2cent.getX()
    circle1y, circle2y = circle1cent.getY(), circle2cent.getY()
    x_dist = circle1x - circle2x
    y_dist = circle1y - circle2y
    return x_dist, y_dist


def main():
    width = 500
    height = 500
    win = GraphWin('Ball Collision Test', 500, 500)

    circle1 = Circle(Point(width / 4, height / 2), 50)
    circle2 = Circle(Point(width / 2, height / 2), 50)

    circle1.setFill('pink')
    circle2.setFill('light blue')
    circle1.setOutline('pink')
    circle2.setOutline('light blue')

    circle1.draw(win)
    circle2.draw(win)

    falseforv1 = hit_horizontal(circle1, win)
    falseforv2 = hit_horizontal(circle2, win)
    falseforv3 = hit_vertical(circle1, win)
    falseforv4 = hit_vertical(circle2, win)

    sidetouchx, sidetouchy, sidetouch2x, sidetouch2y, balltouch = \
        False, False, False, False, False
    xsign, x2sign, ysign, y2sign = get_random(3), get_random(3), get_random(3), get_random(3)

    while falseforv1 is False and falseforv2 is False and falseforv3 \
            is False and falseforv4 is False:
        time.sleep(.01)
        if sidetouchx is True:
            xsign = xsign * -1
        if sidetouchy is True:
            ysign = ysign * -1
        if sidetouch2x is True:
            x2sign = x2sign * -1
        if sidetouch2y is True:
            y2sign = y2sign * -1
        if balltouch is True:
            x_dist, y_dist = cent_dist(circle1, circle2)

            if x_dist > y_dist:
                xsign, x2sign = xsign * -1, x2sign * -1
            elif xsign == 0:
                xsign = y2sign * -1
            elif x2sign == 0:
                x2sign = ysign * -1
            elif ysign == 0:
                ysign = x2sign * -1
            elif y2sign == 0:
                y2sign = xsign * -1
            else:
                ysign, y2sign = ysign * -1, y2sign * -1

        circle1.move(xsign, ysign)
        circle2.move(x2sign, y2sign)
        sidetouchx = hit_horizontal(circle1, win)
        sidetouchy = hit_vertical(circle1, win)
        sidetouch2x = hit_horizontal(circle2, win)
        sidetouch2y = hit_vertical(circle2, win)
        balltouch = did_collide(circle1, circle2)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
