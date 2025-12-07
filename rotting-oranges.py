from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def isValid(x, y):
            return 0 <= x < m and 0 <= y < n and (x, y) not in seen
        m = len(grid)
        n = len(grid[0])
        queue =  deque([])
        fresh = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        
        seen = set(queue)
        ans = 0
        while queue:
            x, y, step = queue.popleft()

            for dx, dy in directions:
                next_row = x + dx
                next_col = y + dy
                if isValid(next_row, next_col) and (next_row, next_col) not in seen:
                    if grid[next_row][next_col] == 1:
                        queue.append((next_row, next_col, step + 1))
                        seen.add((next_row, next_col))
                        fresh.remove((next_row, next_col))
                        ans = max(ans, step+1)
        
        return ans if not fresh else -1


        
