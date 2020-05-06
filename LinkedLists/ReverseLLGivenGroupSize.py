"""Reverse a singly Linked List in groups of given size | Set 3
Given a singly linked list and an integer K, the task is to reverse every
K nodes of the given linked list.
Examples:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL, K = 3
Output: 3 2 1 6 5 4 8 7
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL, K = 5
Output: 5 4 3 2 1 8 7 6

Approach: Two different approaches to solve this problem have been discussed in
Set 1 and Set 2 of this article. In this article, an approach based on deque will be
discussed.
Create a deque.
Store the address of the first k nodes in the deque.
Pop first and the last value from the deque and swap the data values at those addresses.
Repeat step 3 till the deque is not empty.
Repeat step 2 for the next k nodes and till the end of the linked list is not reached.

"""


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def pushInFront(headRef, newVal):
    if headRef is None:
        return LLNode(newVal)

    temp = LLNode(newVal)
    temp.next = headRef
    headRef = temp
    return headRef


def PrintLinkedList(headNode: LLNode):
    if headNode is None:
        print("nothing to print in linked list")
        return

    temp = headNode
    while temp:
        print(temp.data, end=" --> ")
        temp = temp.next
    print("NULL")


# Function to reverse the linked list in groups of
# size k and return the pointer to the new head node.

def ReverseInGroupK(headNode: LLNode, K):
    if not headNode:
        print("Linked list is empty ")
        return

    dq = []
    curr = headNode
    i = 0
    while curr:
        i = 1

        while i <= K:  # Store addresses of the k nodes in the deque
            if curr is None:
                break
            dq.append(curr)
            curr = curr.next
            i += 1
        # pop first and the last value from the deque and swap the data values at
        # those addresses Do this till there exist an address in the deque or deque is not empty
        while len(dq) > 0:
            front = dq[-1]
            last = dq[0]

            front.data, last.data = last.data, front.data
            # 10 --> 9 --> 8 --> 7 --> 6 --> 5 --> 4 --> 3 --> 2 --> 1 --> NULL
            # temp = front.data
            # front.data = last.data
            # last.data = temp

            if len(dq) > 0:
                dq.pop()  # by default it pops and returns from end of list but you can # give index
            if len(dq):
                dq.pop(0)

    return headNode


if __name__ == '__main__':
    # Start with the empty list
    head = None

    # Created Linked list is
    # 1.2.3.4.5.6.7.8.9.10
    head = pushInFront(head, 10)
    head = pushInFront(head, 9)
    head = pushInFront(head, 8)
    head = pushInFront(head, 7)
    head = pushInFront(head, 6)
    head = pushInFront(head, 5)
    head = pushInFront(head, 4)
    head = pushInFront(head, 3)
    head = pushInFront(head, 2)
    head = pushInFront(head, 1)

    print(" original linked list start = ")
    PrintLinkedList(head)

    k = 2

    # Get the new head after reversing the
    # linked list in groups of size k
    head = ReverseInGroupK(head, k)
    print(f" after reversing in group of size k = {k} now Linked List ==")
    PrintLinkedList(head)
