# XOR Linked List – A Memory Efficient Doubly Linked List | Set 2
# In the previous post, we discussed how a Doubly Linked can be created using only one space for
# address field with every node. In this post, we will discuss the implementation of memory
# efficient doubly linked list. We will mainly discuss the following two simple functions.
#
# In the following code, insert() function inserts a new node at the beginning. We need to
# change the head pointer of Linked List, that is why a double pointer is used (See this).
# Let us first discuss few things again that have been discussed in the previous post.
# We store XOR of next and previous nodes with every node and we call it npx, which is the
# only address member we have with every node. When we insert a new node at the beginning,
# npx of new node will always be XOR of NULL and current head. And npx of the current head must
# be changed to XOR of new node and node next to the current head.


# printList() traverses the list in forward direction. It prints data values from every node.
# To traverse the list, we need to get pointer to the next node at every point. We can get the
# address of next node by keeping track of current node and previous node. If we do XOR of
# curr->npx and prev, we get the address of next node.
"""
Traversal of XOR Linked List:
We can traverse the XOR list in both forward and reverse direction. While traversing the list we
need to remember the address of the previously accessed node in order to calculate the next node’s
address. For example when we are at node C, we must have address of B. XOR of add(B) and npx of C
gives us the add(D). The reason is simple: npx(C) is “add(B) XOR add(D)”. If we do xor of npx(C)
with add(B), we get the result as “add(B) XOR add(D) XOR add(B)” which is “add(D) XOR 0” which is
“add(D)”. So we have the address of next node. Similarly we can traverse the list in backward
 direction."""


class LLNode:
    def __init__(self, data):
        self.data = data
        self.npx = 0  # /* XOR of next and previous node */


# /* returns XORed value of the node addresses */
def XORofNodes(a, b):
    return id(a) ^ id(b)


def AddInBeginning(root: LLNode, newVal):
    temp = LLNode(0)
    temp.data = newVal
    temp.npx = XORofNodes(root, LLNode(0))
    if root:
        nxt = XORofNodes(root.npx, LLNode(0))
        root.npx = XORofNodes(temp, nxt)
    root = temp
    return root


def DisplayLL(hdNode: LLNode):
    if hdNode is None:
        return
    curr = hdNode
    prev = LLNode(0)
    nxt = None
    while curr:
        print(curr.data, end=" --> ")
        nxt = XORofNodes(prev, curr.npx)
        prev = curr
        curr = nxt
    print("NULL")


if __name__ == '__main__':
    # Create following Doubly Linked List
    #     head-->40<-->30<-->20<-->10
    head = LLNode(10)
    head = AddInBeginning(head, 20)
    head = AddInBeginning(head, 30)
    head = AddInBeginning(head, 40)

    print('doubly linked list xor memory efficient == :')
    DisplayLL(head)


"""
You can't build an XOR linked list in Python, since Python doesn't let you mess with the bits in 
pointers.

You don't want to implement that anyway -- it's a dirty trick that makes your code hard to 
understand for little benefit.

If you're worried about memory, it's almost always better to use a doubly-linked list with more 
than 1 element per node, like a linked list of arrays.

For example, while an XOR linked list costs 1 pointer per item, plus the item itself, A 
doubly-linked list with 16 items per node costs 3 pointers for each 16 items, or 3/16 pointers 
per item. (the extra pointer is the cost of the integer that records how many items are in the node)
That is less than 1. In Python there are additional overheads, but it still works out better.

In addition to the memory savings, you get advantages in locality because all 16 items in the
 node are next to each other in memory. Algorithms that iterate through the list will be faster.

Note that an XOR-linked list also requires you to allocate or free memory each time you add or 
delete a node, and that is an expensive operation. With the array-linked list, you can do better 
than this by allowing nodes to be less than completely full. If you allow 5 empty item slots, 
for example, then you only have allocate or free memory on every 3rd insert or delete at worst"""