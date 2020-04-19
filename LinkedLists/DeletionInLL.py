# Linked List | Set 3 (Deleting a node)
# We have discussed Linked List Introduction and Linked List Insertion in previous posts on singly
# linked list.
# Let us formulate the problem statement to understand the deletion process. Given a ‘key’,
# delete the first occurrence of this key in linked list.
# To delete a node from linked list, we need to do following steps.
# 1) Find previous node of the node to be deleted.
# 2) Change the next of previous node.
# 3) Free memory for the node to be deleted.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushInBeginning(self, newVal):
        temp = Node(newVal)
        temp.next = self.head
        self.head = temp

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("NULL")

    def DeleteGivenKey(self, keyToDelete):
        temp = self.head
        if temp is None:
            return
        if temp and temp.data == keyToDelete:
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == keyToDelete:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None


if __name__ == '__main__':
    lList = LinkedList()
    lList.pushInBeginning(7)
    lList.pushInBeginning(1)
    lList.pushInBeginning(3)
    lList.pushInBeginning(2)

    print("Created Linked List: ")
    lList.printList()
    lList.DeleteGivenKey(1)
    print("Linked List after Deletion of 1:")
    lList.printList()
