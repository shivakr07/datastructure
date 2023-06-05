# sum of numbers formed by the numbers formed by the numbers formed by the diigits of the path
# like 
'''
        3
       /  \    
      7    1
     /    / \ 
    9    4   5
    
so there are three paths 
    3 7 9   -> path one
    3 1 4   -> path tw0
  + 3 1 5   -> path three
  1 0 0 8   -> there sum
'''
# above are the paths and there sum

# ----------------------------------------------------
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data
        
def print_Preorder(root):
    if root == None:
        return
    print(root.val, end=" ")
    print_Preorder(root.left)
    print_Preorder(root.right)

def pathsum(root, ans,temp):
    if root == None:
        temp.pop()
        return
    if root.left == None and root.right == None:
        temp.append(str(root.val))
        ans.append(temp.copy())
        print("here temp is", temp)
        temp.pop()
        return
    temp.append(str(root.val))
    pathsum(root.left, ans, temp)
    pathsum(root.right, ans, temp)
    
# main block 
if __name__ == "__main__":
    root = Node(3)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(9)
    root.right.left = Node(4)
    root.right.right = Node(5)
    ans = []
    temp = []
    print_Preorder(root)
    pathsum(root, ans, temp)
    print(ans)
    for i in range(len(ans)):
        ans[i] = int("".join(ans[i]))
    print(ans)
    print(sum(ans))
    
        
    
    # calling preorder func to check and printing the tree in preorder format
    