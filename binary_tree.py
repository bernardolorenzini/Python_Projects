class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:

    def __init__(self):
        self.root = Node(None)

    def insert(self, valor):
        if self.root.data is None:
            self.root = Node(valor)
            return

        if self.root.data == valor:
            print("numero ja dentro da arvore")
            return

        if valor < self.root.data:
            if self.root.left:
                self.root.left.insert(valor)
                return
            self.root.left = Node(valor)
            return

        if self.root.right:
            self.root.right.insert(valor)
            return
        self.root.right = Node(valor)



    def printTree(self):
        if self.root is None:
            print("Arvore Vazia")
        else:
            self._printTree(self.root)

    def _printTree(self, node):
        if node.left is None:
            if node.right is None:
                print(node.data)
            else:
                self._printTree(node.right)
        else:
            self._printTree(node.left)


    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals


tree = BinaryTree()

tree.insert(3)
tree.insert(5)
tree.insert(1)
tree.printTree()

