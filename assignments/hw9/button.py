"""
Name: Kaki Newsome
File: button.py

This program creates button in a GUI to be used in three_door_game.py.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""

from graphics import Text, Point, Rectangle

class Button:
    """
    A class that creates buttons and changes color, sets text, and more.
    """
    def __init__(self, shape, label):
        self.shape = shape
        self.text = label

    def get_label(self):
        return self.text

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        left_corner = self.shape.getP1()
        right_corner = self.shape.getP2()
        if point.getX() < left_corner.getX() or point.getX() > right_corner.getX():
            return False
        if point.getY() < left_corner.getY() or point.getY() > right_corner.getY():
            return False
        return True

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text = label
