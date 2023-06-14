# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def pre(root,arr):
            if root == None:
                return
            arr.append(root.val)
            if root.left:
                pre(root.left, arr)
            if root.right:
                pre(root.right, arr)
        pre(root, arr)
        arr.sort()
        if len(arr) == 1:
            return arr[0]
        minm = abs(arr[0]- arr[1])
        for i in range(len(arr)-1):
            
            minm = min(abs(arr[i+1] - arr[i]), minm)
        return minm