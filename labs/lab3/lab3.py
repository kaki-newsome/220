"""
Name: Kaki Newsome
lab3.py
"""


def average():
    num_grade = eval(input("Enter the number of grades you want to input: "))
    acc = 0
    for i in range(1, num_grade + 1):
        grade = eval(input("Enter grade for HW" + str(i) + ": "))
        acc += grade
    avg = acc / num_grade
    print("Your average is", round(avg, 2))


def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("How much would you like to tip? "))
        acc += tip
    print("The total amount made is $", acc)


def newton():
    x = eval(input("Enter the number you want squared: "))
    imp_time = eval(input("Enter the amount of times you want to improve the approximation: "))
    approx = x / 2
    for i in range(imp_time):
        approx = (approx + x / approx) / 2
    print("The square root of", x, "is", approx)


def sequence():
    series_num = eval(input("Enter the number of terms in a sequence: "))
    for i in range(1, series_num + 1):
        seq = 1 + i // 2 * 2
        print(seq, end = "")


def pi():
    n = eval(input("Input the number of terms in the series: "))
    acc = 1
    for i in range(n):
        num = 2 + i // 2 * 2
        den = 1 + (i + 1) // 2 * 2
        acc = acc * (num / den)
    pi = acc * 2
    print("The approximation of pi is", pi)


# average()
# tip_jar()
# newton()
# sequence()
# pi()
