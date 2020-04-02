def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


# def display():
#     print("display function ran")
#
#
# decorator_display = decorator_function(display)  # now this is just as same as making a decorator
# # @decorator_function this is the same thing.
# # display = decorator_function(display) this is also same
# decorator_display()


# we  can write --  this is also same and simply call display function above lines from 9-16 are same as below

# @decorator_function
# def display():
#     print("display function ran")
#
#
# display()
#
#
# # added *args and **kwargs in decorator so that it can accept any number of arguments arbitrary or positional
# @decorator_function
# def display_info(name, age):
#     print('display info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info("ritesh", 21)


# we can make class decorators too we just have to us __init__ method of that class.

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method before {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)

# we can get the same functionality as above just change their names to decoratorClass--
@decorator_class
def display():
    print("display function ran")


display()


# added *args and **kwargs in decorator so that it can accept any number of arguments arbitrary or positional
@decorator_class
def display_info(name, age):
    print('display info ran with arguments ({}, {})'.format(name, age))


display_info("ritesh", 21)
