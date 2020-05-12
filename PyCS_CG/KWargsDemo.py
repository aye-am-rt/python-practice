def kwargs_demo(**kwargs):  # means dictionary
    for k, v in kwargs.items():
        print(f"{k} => {v}")


def args_demo(*args):
    print(*args)
    for ag in args:
        print("ar= ", ag)


def normalTest(arg1, arg2):
    print(arg1)
    print(arg2)


def defaultParametersValue(a, b=9):
    print(a)
    print(b)


# pass by reference also works in python
def MixedArgsKwargs(*args, **kwargs):
    print(*args)
    # print(**kwargs.__repr__())
    for ag in args:
        print("ar= ", ag)
    for k, v in kwargs.items():
        print(f"{k} => {v}")


if __name__ == '__main__':
    kwargs_demo(a=55, b="rt", virat=[1, 2, 3])  # we can pass n number of kwargs and in any order
    # separated by equals, order is not maintained
    args_demo(1, "hello", 3, 5)
    MixedArgsKwargs("a", 1, "hello", b="2", c=2, kw3="9999")  # first args should be given then
    # kwars this is mandatory # it will automatically select args and kwargs

    defaultParametersValue(8, 13)  # if b is given it overrides default if not given default set will be used
    # first positional argument should always be given , default should always be in last in function.
    # defaultParametersValue(d=67, b=765) # variable names should be matched, this line is wrong

    print("******** comprihensions*************")
    lst_Comp = [i * i for i in range(10)]
    setComp = {i * i for i in range(10)}
    dct_comp = {i: i * i for i in range(10)}
    print(lst_Comp)
    print(setComp)
    print(dct_comp)
    lstIfElse = [i * i if i % 2 == 0 else f"{i} is odd" for i in range(20)]
    print(lstIfElse)  # performance is almost sames.

    #  range is a generator , it is lazily evaluated, produce on demand.
    # we can generate infinite values or real time video processing , infinite series etc, sensor readings
    # large files handling ...stream.
    # generate on demand
    # making any function a generator
    def genNums():
        yield 1
        yield 2
        yield 3


    g = genNums()
    print(next(g))
    print(next(g))  # if you call next more than the number of yields it will throw stop iteration error.
    #  you can try and catch execption.
    try:
        print(next(g))
        print(next(g))
    except StopIteration as e:
        print("end of values")

    for i in g:
        print("for runs = ", i)
