class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def print_tree(self):
        if self.root is None:
            print("The tree is empty")
        else:
            self._print_inorder(self.root)
            print()

    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left)
            print(node.value, end=" ")
            self._print_inorder(node.right)

tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

tree.print_tree() 
