"""
Name: Kaki Newsome
File: mean.py

This program encodes a user input statement using the Vigenere cipher.

I just wanted to say I know this is all wrong.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""

from graphics import *


def code(message, keyword):
    msg_code = message.upper()
    msg_code = msg_code.split()

    key_code = keyword.upper()

    msg_acc = ''

    for i in msg_code:
        msg_acc = msg_acc + i

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_acc = 0

    for letter in alphabet:
        



def main():
    win = GraphWin("Encoder", 500, 500)

    msg_ui = Entry(Point(300, 150), 25)
    key_ui = Entry(Point(300, 300), 15)

    msg_text = Text(Point(50, 150), "Message:")
    key_text = Text(Point(50, 300), "Key:")

    outline = Rectangle(Point(200, 350), Point(300, 450))
    butt_text = Text(Point(250, 400), "Encode it!")

    msg_text.draw(win)
    key_text.draw(win)

    msg_ui.draw(win)
    key_ui.draw(win)

    outline.draw(win)
    butt_text.draw(win)

    win.getMouse()

    msg_code = msg_ui.getText()
    key_code = key_ui.getText()

    # print(msg_acc)
    # print(key_code)

    outline.undraw()
    butt_text.undraw()
    # win.getMouse()

    win.getMouse()


if __name__ == '__main__':
    main()
