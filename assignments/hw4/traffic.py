"""
Name: Kaki Newsome
File: mean.py

This program takes user input and outputs the average number of cars travelled
down each road per day, the total number of vehicles, and the average number
of vehicles for all the roads.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""

def main():
    num_road = eval(input("Enter number of roads surveyed: "))
    acc1 = 0
    acc2 = 0

    for i in range(num_road):
        road_days = eval(input("Enter number of days the road was surveyed: "))

        for _ in range(road_days):
            num_cars = eval(input("Enter number of cars in a day: "))
            acc1 = acc1 + num_cars

        acc2 = acc2 + acc1
        road_avg = acc1 / road_days
        acc1 = 0

        print("Road", i, "average vehicles per day:", round(road_avg, 2))
    print("Total number of cars on all roads:", acc2)
    print("Average number of vehicles per road:", round(acc2 / num_road, 2))

if __name__ == '__main__':
    main()
