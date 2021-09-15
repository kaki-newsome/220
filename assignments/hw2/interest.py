"""
Name: Kaki Newsome
File: interest.py

This program calculates the monthly interest charge.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""


def main():
    ann_int = eval(input("Enter the annual interest rate: "))
    ann_int_perc = ann_int / 100
    days = eval(input("Enter the number of days in a billing cycle: "))
    prev_bal = eval(input("Enter the previous net balance: "))
    pay_amt = eval(input("Enter the payment amount: "))
    day_pay = eval(input("Enter the day in the billing cycle when the payment was made: "))

    step1 = days * prev_bal
    step2 = (days - day_pay) * pay_amt
    step3 = step1 - step2
    step4 = step3 / days

    month_charge = step4 * ann_int_perc / 12

    print(round(month_charge, 2))

if __name__ == '__main__':
    main()
