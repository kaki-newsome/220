"""
Name: Kaki Newsome
lab2.py
"""

import math


def sum_of_threes():
    acc = 0
    up_bound = eval(input("What would you like your upper bound to be? "))
    for i in range(0, up_bound + 1, 3):
        acc = acc + i
    print(acc)


def multiplication_table():
    for i in range(1, 11):
        for x in range(1, 11):
            ans = i * x
            print(ans, end=" ")
        print()


def triangle_area():
    a = eval(input("What is the first side length? "))
    b = eval(input("What is the second side length? "))
    c = eval(input("What is the third side length? "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of the triangle is {:.4f}".format(area))


def sumSquares():
    low_range = eval(input("What do you want the lower number to be? "))
    high_range = eval(input("What do you want the higher number to be? "))
    acc = 0
    for i in range(low_range, high_range + 1):
        square = i ** 2
        acc = acc + square
    print("The sum of the squares is", acc)


def power():
    base = eval(input("What is the base number? "))
    exp = eval(input("What is the exponent? "))
    ans = 1
    for i in range(exp):
        ans = ans * base
    print(base, "^", exp, "=", ans)


# sum_of_threes()
# multiplication_table()
# triangle_area()
# sumSquares()
# power()
