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
def preorder_traverse(root):
    if root:
        print(root.data,"->", end=" ")
        preorder_traverse(root.left)
        preorder_traverse(root.right)

def inorder_traverse(root):
    print("in-order traversal")
    if root:
        preorder_traverse(root.left)
        print(root.data,"->", end=" ")
        preorder_traverse(root.right)

def postorder_traverse(root):
    print("post-order traversal")
    if root:
        preorder_traverse(root.left)
        preorder_traverse(root.right)
        print(root.data,"->", end=" ")

# main method
if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
print("pre-order traversal : ",preorder_traverse(tree.root))
print("inorder traversal : ", inorder_traverse(tree.root))
print("postorder traversal : ", postorder_traverse(tree.root))