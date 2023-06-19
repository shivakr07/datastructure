class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def par(length, cntleft, cntright, st, ans):
            
            if len(st) == length:
                ans.append(st)
                print(st)
                return
                
            if cntleft < length//2:
                par(length, cntleft+1, cntright, st+"(", ans)
            if cntright < length//2 and cntright < cntleft:
                par(length, cntleft, cntright+1, st + ")", ans)
            
        ans = []
        par(2*n, 0, 0, "", ans)
        return ans