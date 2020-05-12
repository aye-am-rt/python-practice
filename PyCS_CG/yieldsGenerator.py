def test():
    print("test is called")


def outer(func):
    def inner():
        func()
        pass
    return inner


if __name__ == '__main__':
    k = outer(test)  # just name is given no () with test
    print(k)
    k()

    # any function can be made a decorator and decorators do not change the function definition on which they are
    # being callled they inrease readability and inhance functionality.
    # liker timer functon van be used as decorator.
    # and also stops rewritig same code again and again .
