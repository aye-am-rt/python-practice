class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)

print(len(emp_1))

print(emp_1)  # before defining repr and str method this line would have printed object and some code
# but now its printing str if str is not defined then repr.
print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())  # line 40 and line 43 both are valid and do same thing.
print(emp_1.__str__())

# similar to this  int class and str class both have their __add__ method defined in different way so it works
# differently for them

print(int.__add__(1, 2))
print(str.__add__('1', '2'))
