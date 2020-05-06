import sys


def myMain(inputFileName):
    pass
    # words = parse_file_Function(inputFileName)
    # print(words)


if __name__ == '__main__':
    f = open("newFile.txt", 'w')  # by  default read
    # other mode are x-for error catch , b for binary etc
    try:
        f.write("hola")  # it alsways returns number of chars written in file.
    finally:
        f.close()

    # with is better way to open and write and automatically close the file so use that.
    # it will close the file descriptor for you.

    print("this is a msg", file=f)
    print("this", "can", "be", "done using", "any delimiter", sep="@", end="#", flush=True, file=f)
    print("all process complete")

    # with is called as contact manager and can be used with databases as well.
    # it automatically closes files etc
    with open("newFile.txt", "r") as data:
        for line in data:
            print(line)

    # -------this is  different ----------- #
    myMain(sys.argv[1])  # this is how we call the function with command line argument.
