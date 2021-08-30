'''
Name: Kaki Newsome
lab1.py

Problem: This function calculates the area of a rectangle
'''

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    vol = length * width * height
    print("Volume =", vol)


def shooting_percentage():
    tot_shot = eval(input("How many shots did the player take? "))
    shot_made = eval(input("How many shots were made? "))
    percent = round((shot_made/tot_shot) * 100, 2)
    print("The player's shooting percentage is", percent, "%")

def coffee():
    fix_cost = 1.50
    pounds = eval(input("How many pounds of coffee did you buy? "))
    pound_cost = 10.50
    tot_cost = round(pounds * pound_cost + fix_cost, 2)
    print("The total cost is ${:.2f}".format(tot_cost))

def kilometers_to_miles():
    kilos = eval(input("How many kilometers have you driven? "))
    miles = round(kilos/1.61, 3)
    print("You have driven", miles, "miles.")

# calc_area()
# calc_rec_area()
# calc_volume()
# shooting_percentage()
# coffee()
# kilometers_to_miles()