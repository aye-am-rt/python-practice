import random


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertInLLAtBeginning(hdNode, newValue):
    if hdNode is None:
        return LLNode(newValue)
    else:
        temp = LLNode(0)
        temp.data = newValue
        temp.next = hdNode
        hdNode = temp
        return hdNode


def GenerateRandomLL(ln: int):
    if ln == 0:
        print("length given is zero")
        return None

    # random.seed(3)
    head = LLNode(random.randint(1, 50))
    for i in range(1, ln):
        head = insertInLLAtBeginning(head, random.randint(1, 50))
    return head


def DisplayLL(head: LLNode):
    if head is None:
        return
    else:
        while head is not None:
            print(head.data, end=" --> ")
            head = head.next

    print("NULL")


def appendInLastLL(root, valToAppend):
    if root is None:
        return LLNode(valToAppend)
    temp = root
    while temp.next:
        temp = temp.next
    temp.next = LLNode(valToAppend)
    return root


def MakeMaxOfBoth(rt1, rt2):
    if rt1 is None and rt2 is None:
        print("both lists null")
        return None
    elif rt1 is None and rt2:
        print("list 1 is null")
        return rt2
    elif rt2 is None and rt1:
        print("list 2 is null")
        return rt1
    else:
        newHead = None
        while rt1 and rt2:
            newHead = appendInLastLL(newHead, max(rt1.data, rt2.data))
            rt1 = rt1.next
            rt2 = rt2.next
            # print(max(td1, td2), end=" --> ")
        return newHead


if __name__ == '__main__':
    llL = int(input("give length to randomly generate Linked List ( < 20 ) = ").strip())
    root1 = GenerateRandomLL(llL)
    print(f"1st random linked list of length {llL} ==")
    DisplayLL(root1)
    root2 = GenerateRandomLL(llL)
    print(f"2nd random linked list of length {llL} ==")
    DisplayLL(root2)
    newLL = MakeMaxOfBoth(root1, root2)
    print(f"new linked list by taking max at each position ==")
    DisplayLL(newLL)
