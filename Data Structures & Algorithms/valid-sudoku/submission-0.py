from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rule 1: each row must contain 1-9 without duplicate
        # rule 2: each colum must contain 1-9 wihtout duplicate
        # rule 3: nine 3x3 sub-boxes of the grid must contain the digits 1-9 without duplicates

        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c] 
                    or board[r][c] in sqrs[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqrs[(r//3,c//3)].add(board[r][c])
        
        return True
