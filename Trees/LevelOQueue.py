""" Level Order Tree Traversal
Level order traversal of a tree is BREADTH FIRST TRAVERSAL for the tree."""
#
# Method 1 (Use function to print a given level)
#
# Algorithm:
# There are basically two functions in this method. One is to print all nodes at a given level
# (printGivenLevel), and other is to print level order traversal of the tree (printLevel order).
# printLevel order makes use of printGivenLevel to print nodes at all levels one by one starting
# from root.
""" Function to  print level order traversal of tree 
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

# Print nodes at a given level 
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.data),
    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)"""

# Time Complexity: O(n^2) in worst case. For a skewed tree, printGivenLevel() takes O(n)
# time where n is the number of nodes in the skewed tree. So time complexity of printLevelOrder()
# is O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).

# Space Complexity: O(n) in worst case. For a skewed tree, printGivenLevel() uses O(n) space for
# call stack. For a Balanced tree, call stack uses O(log n) space,
# (i.e., height of the balanced tree).


"""Method 2 (Using queue)

Algorithm:
For each node, first the node is visited and then it’s child nodes are put in a FIFO queue.

printLevel_order(tree)
1) Create an empty queue
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node->data.
        b) Enqueue temp_node’s children (first left then right children) to q
    c) Dequeue a node from q and assign it’s value to temp_node"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


"""Time Complexity: O(n) where n is number of nodes in the binary tree
Space Complexity: O(n) where n is number of nodes in the binary tree"""


def PrintLevelOrdWithQueue(rtNode: Node):
    if not rtNode:
        return

    q = [rtNode]
    while len(q):
        print(q[0].data, end="  ")
        qTopNode = q.pop(0)
        if qTopNode.left:
            q.append(qTopNode.left)
        if qTopNode.right:
            q.append(qTopNode.right)


# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
PrintLevelOrdWithQueue(root)
