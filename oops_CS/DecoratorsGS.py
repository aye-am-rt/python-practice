class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # property decorator allows us to define a method but we can use it as an attribute.
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # without setter python throws error coz it doesnt knows how to set full name from a given string.
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"   # what if we want to set emp name by giving string like this and also want it to
# automatically set first name last name and email of that employee.
# thats why here we use @<any_method_name>.setter or deleter.

print(emp_1.first)
print(emp_1.email)  # if we dont make that a property we have to call it like a method emp1.email()
# that is not good coz it will break the code for other people who was using class before this change.
print(emp_1.fullname)

del emp_1.fullname  # this is way of calling deleter method.
