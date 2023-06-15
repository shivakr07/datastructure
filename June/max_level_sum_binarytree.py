# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root, arr):
            q = []
            q.append(root)
            
            while len(q):
                temp = []
                l = len(q)
                for i in range(l):
                    x = q.pop(0)
                    temp.append(x.val)
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
                arr.append(temp)
        arr = []
        # ans = []
        bfs(root, arr)
        print(arr)
        maxm = sum(arr[0])
        ind = 0
        for i in range(len(arr)):
            if sum(arr[i]) > maxm:
                maxm = sum(arr[i])
                ind = i
            
            # ans.append(maxm)
        return ind+1
#     here we are adding because here level start with 1 not 0