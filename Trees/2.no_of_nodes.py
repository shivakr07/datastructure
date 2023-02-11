#this class creates the nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

#this creates the tree and initially tree have no node so we'll create root and make it None
class BinaryTree:
    def __init__(self):
        self.root = None

#traversal
def countNodes(root):
    if root == None:
        return 0
    return 1 + countNodes(root.left)  + countNodes(root.right)


# main method
if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

ans = countNodes(tree.root)
print("no of nodes in tree are : ", ans)