import random


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# # Function to insert node in linked list
# this is bad because time complexity= O(n^2)  better approach shown below
# def insert(root, item):
#     temp = Node(item)
#
#     if (root == None):
#         root = temp
#     else :
#         ptr = root
#         while (ptr.next != None):
#             ptr = ptr.next
#         ptr.next = temp
#
#     return root


"""Efficient Approach: We traverse array from end and insert every element at the 
beginning of the list."""


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


def DeleteNthFromEnd(head, nFromEnd):
    if head is None:
        print("no linked list present")
        return None

    firstMover = secondMover = head
    for i in range(nFromEnd + 1):
        if firstMover is not None:
            firstMover = firstMover.next
        else:
            print(f"can not delete {nFromEnd}th from end")
            return None

    while firstMover:
        secondMover = secondMover.next
        firstMover = firstMover.next
    secondMover.next = secondMover.next.next
    return head


if __name__ == '__main__':
    llL = int(input("give length to randomly generate Linked List ( < 20 ) = ").strip())
    rtNode = GenerateRandomLL(llL)
    print(f"initial random linked list of length {llL} ==")
    DisplayLL(rtNode)
    delNum = 7
    newLL = DeleteNthFromEnd(rtNode, delNum)
    if newLL:
        print(f"after deleting {delNum} node from last linked list ==")
        DisplayLL(newLL)

    """below is just test for input with map , python 3 use input() not raw_input()
     always print map with list(varName) otherwise it prints map object<0X637376FRT>"""
    # ll2 = map(int, input("give len = ").strip().split(" "))
    # print(list(ll2))
    # give len = 45 67 12 78 ==>[45, 67, 12, 78]
    # if give just one num --> give len = 456 ==> it prints this [456]
    """============ now below if we don't give split() ================="""
    # ll3 = map(int, input("give len = ").strip())
    # give len = 45 ==> it even splits number each character [4, 5] without split
    # print(list(ll3))
    """above is just test for input with map , python 3 use input() not raw_input()"""

    # a = [int(i) for i in input().split()]  this is list Comprehension its faster than normal
    # a = map(int, input().split())
    # x, y = map(int, input().split())
    # x, y = [int(x) for x in input().split()] this is list Comprehension its faster than normal


"""
You have to turn the map into a list or tuple first. To do that,

print(list(F_temps))
This is because maps are lazily evaluated, meaning the values are only computed on-demand. 

Let's see an example

def evaluate(x):
    print(x)

mymap = map(evaluate, [1,2,3]) # nothing gets printed yet
print(mymap) # <map object at 0x106ea0f10>

# calling next evaluates the next value in the map
next(mymap) # prints 1
next(mymap) # prints 2
next(mymap) # prints 3
next(mymap) # raises the StopIteration error
When you use map in a for loop, the loop automatically calls next for you, and treats the 
StopIteration error as the end of the loop. Calling list(mymap) forces all the map values to be
evaluated.

result = list(mymap) # prints 1, 2, 3
However, since our evaluate function has no return value, result is simply [None, None, None]"""
