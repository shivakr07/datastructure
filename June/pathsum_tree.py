# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pre(root, path, arr):
            if root == None:
                return
            
            path.append(root.val)
            if root.left == None and root.right == None:
                arr.append(path[:])
            if root.left:
                pre(root.left, path,arr)
            if root.right:
                pre(root.right, path, arr)
            path.pop(-1)
        path = []
        arr = []
        pre(root, path, arr)
        # print(arr)
        for item in arr:
            # print(item)
            # print(sum(item))
            if sum(item) == targetSum:
                return True
        return False

#  whenever you are applying backtracking then always remove/pop it after the recursion calls 
#machine learning exam is yesterday so creating a fake commit