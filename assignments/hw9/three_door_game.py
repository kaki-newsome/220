"""
Name: Kaki Newsome
File: three_door_game.py

This program allows the user to play a game of choosing between three doors
and randomly chooses a door as the secret door.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""

from random import randint
from graphics import Text, Rectangle, Point, GraphWin
from button import Button


def create_door(number, x_door, height):
    door = Rectangle(Point(x_door - 50, height / 2 - 70),
                     Point(x_door + 50, height / 2 + 70))
    label = Text(Point(x_door, height / 2), "Door" + str(number))
    return Button(door, label)


# def create_label(number, x_door, height):
#     return Text(Point(x_door, height / 2), "Door" + str(number))


def main():
    width = 500
    height = 500
    win = GraphWin("Three door game", width, height)

    button_list = []
    for i in range(1, 4):
        x_door = 127 * i
        button = create_door(i, x_door, height)
        button_list = button_list + [button]

    for door in button_list:
        door.draw(win)

    point = win.getMouse()
    rand = randint(1, 3)
    win_text = Text(Point(width / 2, 20), "You win! Door " + str(rand) + " is the "
                                                                         "secret door")
    lose_text = Text((Point(width / 2, 20)), "You lost. Door " + str(rand) + " is the "
                                                                             "secret door")
    for i in range(3):
        clicked = button_list[i].is_clicked(point)
        if clicked is True:
            if rand - 1 == i:
                button_list[i].color_button('green')
                win_text.draw(win)
            else:
                button_list[i].color_button('red')
                lose_text.draw(win)

    win.getMouse()


if __name__ == '__main__':
    main()
