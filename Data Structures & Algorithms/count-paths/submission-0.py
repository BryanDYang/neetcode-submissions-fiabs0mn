class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(r, c, rows, cols):
            if r == rows or c == cols:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            
            return (dfs(r + 1, c, rows, cols) + 
                    dfs(r, c + 1, rows, cols))

        return  dfs(0, 0, m, n)
        