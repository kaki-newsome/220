"""
Name: Kaki Newsome
lab12.py
"""
from random import randint


def find_and_remove_first(list, value):
    try:
        i = list.index(value)
        list[i] = "kaki"
    except:
        pass
    print(list)

def good_input():
    x = eval(input("enter a number 1-10: "))
    while x >= 1 or x <= 10:
        return x

def num_digits():
    num = eval(input("enter a number greater than 0, 0 or less to quit: "))
    while num > 0:
        digits = 0
        while num != 0:
            num //= 10
            digits += 1
        print("The number has " + str(digits) + " digit/s.")
        num = eval(input("Enter a number greater than 0, 0 or less to quit: "))

def hi_lo_game():
    secret = randint(1, 100)
    guess = 1
    num = eval(input("Guess the secret number: "))
    while guess < 7 and num != secret:
        guess += 1
        if num > secret:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        num = eval(input("Enter a number greater than 0, 0 or less to quit: "))
    if num == secret:
        print("You won, the number was " + str(secret) + " it took you " + str(guess)
              + " guesses")
    else:
        print("You lost, the number was " + str(secret))
def read_data(filename):
    file = open(filename, 'r')
    data = file.read()
    data = data.split()
    return data

def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val in values:
            return True
        i += 1
    return False


def main():
    # find_and_remove_first(["hello", "penguin", "bop", "doom"], "bop")
    # good_input()
    # num_digits()
    # hi_lo_game()
    is_in_linear("20", read_data("dataSorted.txt"))
main()
