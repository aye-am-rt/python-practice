class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def FindPreSuc(rt, inQl):
    if rt is None:
        return

    FindPreSuc(rt.left, inQl)
    inQl.append(rt.data)
    FindPreSuc(rt.right, inQl)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    ql = []
    if ql:
        print("empty true")
    target = 5
    FindPreSuc(root, ql)
    print(ql)
    if target in ql:
        if ql[0] == target:
            print(f"predecessor= None successor= {ql[1]}")
        elif ql[-1] == target:
            print(f"predecessor= {ql[-2]} successor= None")
        else:
            indexT = ql.index(target)
            print(f"predecessor= {ql[indexT - 1]} successor= {ql[indexT + 1]}")
