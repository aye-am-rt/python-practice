# instance Variables -- vars that are for objects of that class they can be unique for all objects(instance).
# class Variables -- vars that are just in class they can be used by its objects but their value initially
# will be same for everyone, every object.

# sometimes its better to make something that all objects of a class will have. so then you make a class variable.
# you can print namespace of any object or the class itself by printing __dict__.

# class variables can be accessed through instance of the class or class itself.
# like Employee.var_name or self.var_name


class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('ritesh', 'tiwari', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# it would be better if we can access raise amount,since we made it class var we can access it otherwise not possible
# print(emp_1.raise_amount)
# print(Employee.raise_amount)

if __name__ == '__main__':
    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)
    print(emp_1.raise_amount)
    print(Employee.raise_amount)
    print(emp_1.__dict__)  # namespace- you can see there is no raise_amount in emp1 or emp2 namespace
    print(Employee.__dict__)  # there will be raise_amount in Employee namespace.
    print(emp_2.__dict__)  # but still in line 39 i was able to access raise amount coz it first checked in instance
    # then class itself and found it there.

    # now if we change Employee.raise_amount it will change for all. but of we change it for emp1.raise amount or
    # emp2.raise_amount it will change just for that instances.

    Employee.raise_amount = 1.05
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    print("********************")
    emp_1.raise_amount = 1.9  # now after doing this raise_amount will come in emp1 namespace print and see.
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    print(emp_1.__dict__)
    print(emp_2.__dict__)
    print('num of employee objects created = ', Employee.num_of_emps)
