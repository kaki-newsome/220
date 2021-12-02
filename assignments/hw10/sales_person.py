"""
Name: Kaki Newsome
File: sales_person.py

This program creates a class SalesPerson that makes a sales person to be used in
python file sales_force.py.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        """
        constructor for SalesPerson
        """
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """
        returns id of sales person
        """
        return self.employee_id

    def get_name(self):
        """
        returns name of sales person
        """
        return self.name

    def set_name(self, name):
        """
        sets name of sales person
        """
        self.name = name

    def enter_sale(self, sale):
        """
        adds a sale to the sales person
        """
        self.sales += [sale]

    def total_sales(self):
        """
        calculates all the sales of the sales person
        """
        sum = 0
        for num in self.sales:
            sum += num
        return sum

    def get_sales(self):
        """
        returns list of all sales of sales person
        """
        return self.sales

    def met_quota(self, quota):
        """
        returns True if total sales met quota or exceeded, false otherwise
        """
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        """
        compares total sales of one sales person to another sales person
        """
        if other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() < self.total_sales():
            return 1
        return 0

    def __str__(self):
        """
        returns string of sales person information
        """
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())
