# regular methods inside class automatically just take the instance of that class as first argument.
# to change that so it takes class as its first argument use decorator @classmethod


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # sometimes classmethods can be used as alternative constructors. the better example of this is datetime
    # module of python you can make a date object by passing date or time in various ways.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.strip(' ').split('-')
        return cls(first, last, int(pay))

    # static method dont use 'self' or 'cls' they just have to do something with logic of a class something
    # to return a checkpoint or something. static methods have some logical connection with the class.they dont take
    # any instance or class as first argument
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)  # it will change raise amount for every object and class itself.
emp_1.set_raise_amt(1.05)  # this will also change the amount for everyone coz its like setter method.
# and you just executed it.

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve--Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
print(emp_str_2.split('-'))
first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
