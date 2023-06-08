class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def recurs(board, word, row, col, level):
            if level == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            
            if board[row][col] == word[level]:
                board[row][col] = '$'
                # board[row].replace(mat[row][col], "$")
                
                retval = (recurs(board, word, row - 1, col,  level + 1) |
                          recurs(board, word, row + 1, col,  level + 1) |
                          recurs(board, word, row, col - 1,  level + 1) |
                          recurs(board, word, row, col + 1,  level + 1))
            
                board[row][col] = word[level]
                return retval
            else:
                return False
        def find(board,word):
            if len(word) >  (len(board) * len(board[0])):
                return False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    
                    if board[i][j] == word[0]:
                        if recurs(board, word, i, j, 0):
                            return True
            return False
        return find(board, word)