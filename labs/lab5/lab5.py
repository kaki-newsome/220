"""
Name: Kaki Newsome
lab5.py
"""

from graphics import *
from math import sqrt

def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    triangle = Polygon(p1, p2, p3)

    triangle.draw(win)
    # and display its area in the graphics window.

    a_x = p1.getX() - p2.getX()
    b_x = p2.getX() - p3.getX()
    c_x = p3.getX() - p1.getX()

    a_y = p1.getY() - p2.getY()
    b_y = p2.getY() - p3.getY()
    c_y = p3.getY() - p1.getY()

    a_len = sqrt(a_x ** 2 + a_y ** 2)
    b_len = sqrt(b_x ** 2 + b_y ** 2)
    c_len = sqrt(c_x ** 2 + c_y ** 2)

    per = a_len + b_len + c_len
    s = (a_len + b_len + c_len) / 2
    area = sqrt((s * (s - a_len) * (s - b_len) * (s - c_len)))

    per_text = Text(Point(250, 10), ("perimeter is", round(per, 2)))
    area_text = Text(Point(250, 30), ("area is", round(area, 2)))

    per_text.draw(win)
    area_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # Entry making
    user_red = Entry(Point(win_width / 2, win_height / 2 + 40), 3)
    user_green = Entry(Point(win_width / 2, win_height / 2 + 70), 3)
    user_blue = Entry(Point(win_width / 2, win_height / 2 + 100), 3)

    user_red.draw(win)
    user_green.draw(win)
    user_blue.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # loop to change color of circle
    for i in range(5):
        win.getMouse()  # need to have to stop loop
        red_val = eval(user_red.getText())
        green_val = eval(user_green.getText())
        blue_val = eval(user_blue.getText())

        color = color_rgb(red_val, green_val, blue_val)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s1 = input("Enter a string: ")

    print(s1[0])
    print(s1[-1])
    print(s1[2:6])
    print(s1[0] + s1[-1])
    print(s1[:3] * 10)
    for i in s1:
        print(i)
    print(len(s1))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = x[:2] + [values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = len(values)
    print(x)

def another_series():
    num_term = eval(input("Enter the number of terms: "))
    acc = 0
    string = ''

    for i in range(num_term):
        num = eval(input("Enter the term: "))
        acc = acc + num
        string = str(num) + ' ' + string

    print(string)
    print("sum =", acc)

def main():
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()

main()
