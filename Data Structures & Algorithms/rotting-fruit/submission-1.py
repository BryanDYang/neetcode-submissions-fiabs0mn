class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        q = collections.deque()

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        

        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q and fresh > 0:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()

                for dr, dc in direct:
                    nr, nc = r + dr, c + dc
                    if(0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1