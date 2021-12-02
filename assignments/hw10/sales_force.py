"""
Name: Kaki Newsome
File: sales_force.py

This program creates creates a class SalesForce that encapsulates data for a sales
person.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""

from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        for line in file:
            line = line.split(',')
            id = int(line[0])
            pre_name = line[1]
            name = pre_name[1:]
            person = SalesPerson(id, name)
            self.sales_people += [person]
            sales = line[2]
            sales = sales[1:]
            sales = sales[:-1]
            sales = sales.split(' ')
            for sale in sales:
                person.enter_sale(float(sale))

    def quota_report(self, quota):
        self.a_list = []
        for person in self.sales_people:
            b_list = []
            b_list += [person.get_id()] + [person.get_name()] + \
                      [person.total_sales] + [person.met_quota(quota)]
            self.a_list += [b_list]
        return self.a_list

    def top_seller(self, SalesPerson):
        top = self.a_list[0]
        top_list = []
        for person in self.a_list:
            if person.total_sales() > top.total_sales():
                top = person
            elif person.total_sales() == top.total_sales():
                top_list += [top] + [person]
        return top

    def individual_sales(self, employee_id):
        for person in self.a_list:
            if person.get_id() == employee_id:
                return person.get_name()
        return None
