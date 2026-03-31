class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        q = deque()

        Rows, Cols = len(grid), len(grid[0])
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in direct:
                    row, col = r + dr, c + dc
                    if (0 <= row < Rows and 0 <= col < Cols and
                        grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
                 