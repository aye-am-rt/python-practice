class BinaryTree:
    def __init__(self, key):
        self.val = key
        self.left = self.right = None


def print_tree_elements(node):
    if node is None:
        return
    print_tree_elements(node.left)
    print(node.val, end=" ")
    print_tree_elements(node.right)


def insert_in_tree(root, data_node):
    if root is None:
        root = data_node
    elif root.val < data_node.val:
        if root.right is None:
            root.right = data_node
        else:
            insert_in_tree(root.right, data_node)
    elif root.left is None:
        root.left = data_node
    else:
        insert_in_tree(root.left, data_node)


def delete_leaf_node(root_node, d_node):
    q = [root_node]
    while len(q):
        temp_node = q.pop(0)
        if temp_node is d_node:
            return
        if temp_node.right:
            if temp_node.right is d_node:
                temp_node.right = None
                return
            else:
                q.append(temp_node.right) 
        if temp_node.left:
            if temp_node.left is d_node:
                temp_node.left = None
                return
            else:
                q.append(temp_node.left)


def delete_in_between(root_node, key):
    if root_node is None:
        return None
    if root_node.left is None and root_node.right is None:
        if root_node.key == key:
            return None
        else:
            return root_node
    key_node = None
    q = [root_node]
    while len(q):
        temp_node = q.pop(0)
        if temp_node.val == key:
            key_node = temp_node
        if temp_node.left:
            q.append(temp_node.left)
        if temp_node.right:
            q.append(temp_node.right)
    if key_node:
        x = temp_node.val
        delete_leaf_node(root_node, temp_node)
        key_node.val = x
    return root_node


rt = BinaryTree(10)
insert_in_tree(rt, BinaryTree(50))
insert_in_tree(rt, BinaryTree(5))
insert_in_tree(rt, BinaryTree(25))
insert_in_tree(rt, BinaryTree(30))

print_tree_elements(rt)
rt = delete_in_between(rt, 50)
print("\nafter deletion")
print_tree_elements(rt)
