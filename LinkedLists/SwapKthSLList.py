# Swap Kth node from beginning with Kth node from end in a Linked List
# Given a singly linked list, swap kth node from beginning with kth node from end. Swapping of
# data is not allowed, only pointers should be changed. This requirement may be logical in many
# situations where the linked list data part is huge (For example student details line Name,
# RollNo, Address, ..etc). The pointers are always fixed (4 bytes for most of the compilers).

# The problem seems simple at first look, but it has many interesting cases.
#
# Let X be the kth node from beginning and Y be the kth node from end. Following are the
# interesting cases that must be handled.
# 1) Y is next to X
# 2) X is next to Y
# 3) X and Y are same
# 4) X and Y don’t exist (k is more than number of nodes in linked list)


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def AddInBeginning(root: LLNode, newVal):
    if root is None:
        return LLNode(newVal)
    temp = LLNode(0)
    temp.data = newVal
    temp.next = root
    root = temp
    return root


def DisplayLL(head: LLNode):
    if head is None:
        return
    while head:
        print(head.data, end=" --> ")
        head = head.next
    print("NULL")


def CountNodesInLL(head: LLNode):
    if head is None:
        return 0
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def SwapKthFromBothEnds(LlHead, kToSwap):
    if LlHead is None:
        print("no linked list present")
        return
    nodeCount = CountNodesInLL(LlHead)

    if nodeCount < kToSwap:
        print("swapping value must not be greater than total nodes")
        return
    if (2 * kToSwap - 1) == nodeCount:
        print("both nodes are same to swap")
        return

    kBeg = LlHead  # Find the kth node from beginning of linked list. We also find previous of
    kBeg_prev = None  # kth node because we need to update next pointer of the previous.
    for j in range(kToSwap - 1):
        kBeg_prev = kBeg
        kBeg = kBeg.next

    kEnd = LlHead  # kth node from end is (n-k+1)th node from beginning
    kEnd_prev = None
    for j in range(nodeCount - kToSwap):
        kEnd_prev = kEnd
        kEnd = kEnd.next

    if kBeg_prev:
        kBeg_prev.next = kEnd
    if kEnd_prev:
        kEnd_prev.next = kBeg

    temp = kBeg.next
    kBeg.next = kEnd.next
    kEnd.next = temp
    if kToSwap == 1:
        LlHead = kEnd
    if kToSwap == nodeCount:
        LlHead = kBeg
    return LlHead


if __name__ == '__main__':
    # Driver Code
    # llist = LinkedList()
    lList = None
    for i in range(8, 0, -1):
        lList = AddInBeginning(lList, i)
    # llist.printList()
    DisplayLL(lList)

    for i in range(1, 9):
        # llist.swapKth(i)
        lList = SwapKthFromBothEnds(lList, i)
        print("Modified List for k = ", i)
        DisplayLL(lList)
