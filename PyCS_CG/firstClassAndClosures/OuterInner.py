def outer_function():
    message = 'Hi'  # this is what we call as a free variable.

    def inner_function():
        print(message)  # inner function can access that free variable

    # return inner_function()  # here we are returning function and executing it at the same time. by removing the
    # () we can simply return the function and assign it to some variable.
    return inner_function


my_func = outer_function()  # this variable is just waiting for executed.
# my_func()
# my_func()
# my_func()  # this is called CLOSURE -- it remembers even after outer function has been done running.


def second_outer_function(msg):
    message = msg

    def second_inner_function():
        print(message)

    return second_inner_function


hi_func = second_outer_function('hi')
bye_func = second_outer_function('bye')

hi_func()
bye_func()
