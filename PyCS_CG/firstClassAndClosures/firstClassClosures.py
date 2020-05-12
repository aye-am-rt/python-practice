# Decorators
# decorators are functions that take in a function... add some extra functionality to it
# and just return the function.

# first class functions --
#  first class functions allow us to treat functions like any other objects.
# pass functions, return functions and assign them to any other variable, that is ready to be executed.

from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)  # if we dont wrap it with orignalfunc it will always show wrapper is being called.
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Tom', 22)
display_info('ritesh', 20)
