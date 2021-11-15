"""
Name: Kaki Newsome
hangman.py
"""
from random import randint


def words(filename):
    infile = open(filename, 'r')

    content = infile.read()
    return content.split('\n')


def random_int(secret_word):
    return secret_word[randint(0, len(secret_word)) - 1]


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def won(word, letters):
    ...
    x = fill(word, letters)
    if word == x:
        return True
    else:
        return False


def play():
    word_list = words('wordlist.txt')
    secret = random_int(word_list)
    incorrect = 0
    current = "_" * len(secret)
    guesses = []
    win = won(secret, guesses)
    while incorrect < 7 and win is False:
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input("What letter do you guess? ")
        while letter in guesses:
            letter = input("Choose a different letter: ")

        guesses = guesses + [letter]

        display = fill(secret, guesses)
        if letter not in secret:  # use current and display
            incorrect += 1
        else:
            current = display

        win = won(secret, current)
    print(display)


def main():
    play()


main()
