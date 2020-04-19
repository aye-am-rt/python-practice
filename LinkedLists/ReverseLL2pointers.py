# We have seen how to reverse a linked list in article Reverse a linked list. In iterative
# method we had used 3 pointers prev, cur and next. Below is an interesting approach that uses
# only two pointers. The idea is to use XOR to swap pointers.
#
# Given pointer to the head node of a linked list, the task is to reverse the linked list.
# Examples:
# Input : Head of following linked list
# 1->2->3->4->NULL
# Output : Linked list should be changed to,
# 4->3->2->1->NULL


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def ReverseLL(head: LLNode):  # NOT WORKING BEKAR METHOD GEEKS.
    prev = None
    current = head
    # This expression evaluates from left to right
    # current->next = prev, changes the link from next to prev node
    # prev = current, moves prev to current node for next reversal of node
    nxt, current.next = current.next, prev
    prev, current = current, nxt
    head = prev
    return head


def push(head: LLNode, new_data):
    if head is None:
        return LLNode(new_data)

    temp = LLNode(new_data)
    temp.next = head
    head = temp
    return head


def printList(head: LLNode):
    temp = head
    while temp:
        print(temp.data, end=" --> ")
        temp = temp.next
    print("NULL")


# NOT WORKING BEKAR METHOD GEEKS.
if __name__ == '__main__':
    lList = LLNode(0)
    lList = push(lList, 20)
    lList = push(lList, 4)
    lList = push(lList, 15)
    lList = push(lList, 85)

    print("original linked list  =")
    printList(lList)
    RevHead = ReverseLL(lList)
    print("after reversing linked list changed = ")
    printList(RevHead)
