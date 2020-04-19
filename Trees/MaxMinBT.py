# Find maximum and minimum element in binary tree without using recursion or stack or queue
# Given a binary tree. The task is to find out the maximum and minimum element in a binary tree
# without using recursion or stack or queue i.e, space complexity should be O(1).

# Prerequisite : Inorder Tree Traversal without recursion and without stack (Morris tree traversal)
# Approach :
# 1. Initialize current as root
# 2. Take to variable max and min
# 3. While current is not NULL
#
# If the current does not have left child
# Update variable max and min with current’s data if required
# Go to the right, i.e., current = current->right
# Else
# Make current as the right child of the rightmost node in current’s left subtree
# Go to this left child, i.e., current = current->left

from sys import maxsize

INT_MAX = maxsize
INT_MIN = -maxsize

print(INT_MAX)
print(INT_MIN)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def PrintMinMaxUsingMorris(root: Node):
    if root is None:
        print(" root is empty ..returning")
        return
    current = root
    pre = Node(0)

    max_found = INT_MIN
    min_found = INT_MAX

    while current is not None:
        if current.left is None:
            max_found = max(max_found, current.data)
            min_found = min(min_found, current.data)
            print(current.data, end="  ")
            current = current.right
        else:
            pre = current.left
            while pre.right is not None and pre.right is not current:
                pre = pre.right

            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                max_found = max(max_found, current.data)
                min_found = min(min_found, current.data)
                print(current.data, end="  ")
                current = current.right

    print("\nMax value is :", max_found)
    print("Min value is :", min_found)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)


rt = Node(15)
rt.left = Node(19)
rt.right = Node(11)

rt.right.left = Node(25)
rt.right.right = Node(5)

rt.right.left.left = Node(17)
rt.right.left.right = Node(3)
rt.right.right.left = Node(23)
rt.right.right.right = Node(24)

PrintMinMaxUsingMorris(rt)

# Space complexity: O(1)
