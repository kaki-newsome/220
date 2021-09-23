"""
Name: Kaki Newsome
File: mean.py

This program takes user input and outputs the RMS average, harmonic mean, and
geometric mean.

Certification of Authenticity:
I certify this assignment is entirely my own.

pseudocode:
1. This program takes user input and outputs the RMS average, harmonic mean, and
geometric mean.
2. The input is the number of terms, and what the terms are, and the output is
the different types of means
3. ask user input, use a loop to ask user for each number, use each number in each
type of mean, get the final values for each mean, print out the means
"""

from math import sqrt

def main():
    terms = eval(input("Enter the number of terms you want to enter: "))
    rms_nums = 0
    harm_nums = 0
    geom_nums = 1

    for _ in range(1, terms + 1):
        num = eval(input("Enter here: "))
        rms_nums = rms_nums + num ** 2
        harm_nums = harm_nums + 1 / num
        geom_nums = geom_nums * num

    rms = sqrt(rms_nums / terms)
    harm_mean = terms / harm_nums
    geom_mean = geom_nums ** (1 / terms)

    print(round(rms, 3))
    print(round(harm_mean, 3))
    print(round(geom_mean, 3))


if __name__ == '__main__':
    main()
