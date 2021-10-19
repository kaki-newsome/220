"""
Name: Kaki Newsome
File: mean.py

This program encodes a user input statement using the Vigenere cipher.

I just wanted to say I know this is all wrong.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""

from graphics import *


def sentence():
    sent = eval(input("Enter message you want to be encoded: "))
    return sent


def key():
    key = eval(input("Enter a key to encode with: "))
    return key


def entry1():
    msg_butt = Entry(Point(300, 150), 25)
    return msg_butt


def entry2():
    key_butt = Entry(Point(300, 300), 15)
    return key_butt


def button():
    outline = Rectangle(Point(200, 350), Point(300, 450))
    return outline


def butt_text():
    butt_text = Text(Point(250, 400), "Encode it!")
    return butt_text


def msg_text():
    msg_text = Text(Point(50, 150), "Message:")
    return msg_text


def key_text():
    key_text = Text(Point(50, 300), "Key:")
    return key_text


def message_change():
    sent = sentence()
    sent = sent.upper()
    return sent


def main():
    win = GraphWin("Encoder", 500, 500)

    msg_text().draw(win)
    key_text().draw(win)

    entry1().draw(win)
    entry2().draw(win)

    button().draw(win)
    butt_text().draw(win)

    # button().undraw()
    # butt_text().undraw()
    # win.getMouse()

    print(message_change())

    win.getMouse()


if __name__ == '__main__':
    main()
