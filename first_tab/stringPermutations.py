resultSet = set()


def allPerm(st1, st0):
    if len(st1) is 0:
        resultSet.add(st0)
        return resultSet
    for i in range(len(st1)):
        allPerm(st1[:i] + st1[i+1:], st0 + st1[i])
    return resultSet


if __name__ == "__main__":
    string1 = "rrt"
    string0 = ""
    print(allPerm(string1, string0))
