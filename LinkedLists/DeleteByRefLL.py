# Given only a pointer/reference to a node to be deleted in a singly linked list,
# how do you delete it?
# Given a pointer to a node to be deleted, delete the node. Note that we
# don’t have pointer to head node.
"""
A simple solution is to traverse the linked list until you find the node you want to delete.
But this solution requires pointer to the head node which contradicts the problem statement.

Fast solution is to copy the data from the next node to the node to be deleted and delete the
next node. Something like following."""


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


def DisplayLL(hdNode: LLNode):
    if hdNode is None:
        return
    while hdNode:
        print(hdNode.data, end=" --> ")
        hdNode = hdNode.next
    print("NULL")


def DeleteNodeByRef(delNode: LLNode):
    prev = None
    if delNode is None:
        return
    else:
        while delNode.next:
            delNode.data = delNode.next.data
            prev = delNode
            delNode = delNode.next
        prev.next = None


if __name__ == '__main__':
    # construct the below linked list
    # 1->12->1->4->1
    head = LLNode(1)
    head = AddInBeginning(head, 4)
    head = AddInBeginning(head, 561)
    head = AddInBeginning(head, 12)
    head = AddInBeginning(head, 13)

    print('list before deleting:')
    DisplayLL(head)

    # deleting the first node in the list
    # delete_node(head.next)
    DeleteNodeByRef(head.next.next)

    print('list after deleting: ')
    DisplayLL(head)
    # print_list(head)

# I wonder whether there is a shortcut to make a simple list out of list of lists in Python.
#
# I can do that in a for loop, but maybe there is some cool "one-liner"?
# I tried it with reduce(), but I get an error.
# ANSWER == STACK OVERFLOW ===>
# Given a list of lists l,
# flat_list = [item for sublist in l for item in sublist]
#
# which means:
# flat_list = []
# for sublist in l:
#     for item in sublist:
#         flat_list.append(item)
