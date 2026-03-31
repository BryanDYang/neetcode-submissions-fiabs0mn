# from functools import lru_cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
                return 0
        cache = [[-1]*cols for _ in range(rows)]

        # @lru_cache(None)
        def dfs(r, c):
            if r >= rows or c >= cols:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if cache[r][c] != -1:
                return cache[r][c]

            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)

            return cache[r][c]

        return dfs(0, 0)