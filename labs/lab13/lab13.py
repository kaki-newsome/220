"""
Name: Kaki Newsome
lab13.py
"""
from graphics import Rectangle, Point

def is_in_binary(search_val, values):
    values.sort()
    midpoint = values[len(values) // 2]
    while midpoint != search_val and len(values) != 1:
        if midpoint > search_val:
            values = values[:len(values) // 2]
        else:
            values = values[len(values) // 2 + 1:]

        midpoint = values[len(values) // 2]

    if len(values) == 1 and values[0] != search_val:
        return False
    return True

def selection_sort(values):
    for i in range(len(values)):
        pos = i
        lowest = values[i]
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]
    return values

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    dict = {}
    areas = []
    for rect in rectangles:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
        selection_sort(areas)
        for i in range(len(areas)):
            rectangles[i] = dict[areas[i]]
    return rectangles

def star_find(filename):
    file = open(filename, 'r')
    signals = file.read().split()
    in_range = []
    for i in range(len(signals)):
        pos = i
        if float(signals[i]) < 5000 and float(signals[i]) > 4000:
            in_range.append(float(signals[i]))
        if len(in_range) == 5:
            break
    print("found " + str(len(in_range)) + " signals within 4000 and 5000")
    print(in_range)
    if len(in_range) < 5:
        print("did not find 5 signals")
    else:
        print("last position of signal found was " + str(pos))




def main():
    # print(is_in_binary(1, [1, 4, 6, 7, 12, 15, 17]))
    # print(selection_sort([2, 5, 3, 1, 4]))
    # print(rect_sort([Rectangle(Point(0, 10), Point(10, 0)),
    #            Rectangle(Point(0, 3), Point(3, 0)),
    #            Rectangle(Point(0, 9), Point(9, 0))]))
    # star_find("signals.txt")

main()
