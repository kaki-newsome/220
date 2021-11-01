"""
Name: Kaki Newsome
lab9.py
"""
# a void function is a function that returns nothing
import math

from graphics import *

def addten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
    # print(nums)

def squareeach(nums):
    # print(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    # print(nums)

def sumList(nums):
    acc = 0
    # print(nums)
    for i in range(len(nums)):
        acc += nums[i]
    # print(nums)
    return acc

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])
    # print(strList)

def writeSumOfSquares():
    infile = open('lab9.txt', 'r')
    outfile = open('lab9out.txt', 'w+')

    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareeach(nums)
        summed = sumList(nums)
        outfile.write('sum of squares = ' + str(summed) + '\n')

def starter():
    weight = float(input("Enter weight: "))
    numwins = int(input("Enter number of wins: "))

    if weight >= 150 and weight < 160 and numwins >= 5:
        print('starter')
    elif weight > 199 or numwins > 20:
        print('starter')
    else:
        print('on the bench')

def leapYear(year):
    if year % 400 == 0:
        print(str(year) + ' is a leap year')
    else:
        print(str(year) + ' is not a leap year')

def circleOverlap():
    win = GraphWin('circle overlap', 500, 500)

    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r1)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    dist = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if r1 + r2 >= dist:
        text1 = Text(Point(250, 450), 'circles overlap')
        text1.draw(win)
    else:
        text2 = Text(Point(250, 450), 'circles dont overlap')
        text2.draw(win)

    win.getMouse()
    win.close()

def main():
    # addten([3, 5, 11])
    # squareeach([3, 5, 11])
    # sumList([3, 5, 11])
    # toNumbers(['3', '5', '11'])
    # writeSumOfSquares()
    # starter()
    # leapYear(2004)
    # circleOverlap()

main()
