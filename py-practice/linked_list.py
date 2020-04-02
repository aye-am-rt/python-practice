class LinkedList:
    def __init__(self, val):
        self.value = val
        self.next = None


def print_linked_list(root_node):
    if root_node and root_node.next:
        print(root_node.value, end=" -> ")
        print_linked_list(root_node.next)
    else:
        print(root_node.value)


def insert_new_node(root_node, new_node=None):
    if root_node is None:
        return
    else:
        while root_node.next:
            root_node = root_node.next
        root_node.next = new_node


def insert_anywhere(root_node, insert_after, new_value=None):
    if root_node is None:
        return
    else:
        while root_node.next:
            if root_node.value == insert_after:
                temp_node = root_node.next
                root_node.next = LinkedList(new_value)
            else:
                temp_node = None
            root_node = root_node.next
        if temp_node:
            root_node.next = temp_node
        else:
            insert_new_node(root_node, LinkedList(new_value))


if __name__ == "__main__":
    root = LinkedList(56)
    insert_new_node(root, LinkedList(34))
    insert_new_node(root, LinkedList(4))
    insert_new_node(root, LinkedList(64))
    insert_new_node(root, LinkedList(234))

    print("Traversing the Linked list")
    print_linked_list(root)
    insert_anywhere(root, 34, 89)
    print_linked_list(root)
