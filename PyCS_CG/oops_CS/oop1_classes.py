# classes allow  us to logically group data and function in a way that is easy to reuse and easy to build up
# on --- data and functions means attributes and methods.


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    # self is an instance getting passed automatically. so every function of any class has an instance of
    # class with it if you don't pass it ,it will throw error. saying zero positional arguments were passed.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('ritesh', 'tiwari', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

if __name__ == '__main__':
    print(emp_1.email)
    print(emp_2.email)
    print(emp_1.fullname())  # ---------------------> 1
    print("*********we can call it by className and then method also--like below--******")
    # *********we have to pass instance name means any object that has been created ******
    print(Employee.fullname(emp_2))  # -------------------> 2
    # so in equation 1 and 2 in 1 it first knows the instance then calls the method but in
    # equation 2 first you call the method then you pass the instance which you want to call it for.
