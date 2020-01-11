if __name__ == "__main__":
    l1 = [int(x) for x in input("give space separated numbers for list 1 = ").split()]
    l2 = [int(x) for x in input("give space separated numbers for list 2 = ").split()]

    l1.extend(l2)
    print(sorted(l1))
