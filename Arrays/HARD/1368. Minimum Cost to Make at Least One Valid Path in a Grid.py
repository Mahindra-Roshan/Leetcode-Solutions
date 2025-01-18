class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        visited= set()
        queue =deque([(0, 0, 0)])
        while True:
            i, j, cost = queue.pop()
            if 0 <= i < n and 0 <= j < m and not (i, j) in visited:
                visited.add((i, j))
                if i == n - 1 and j == m - 1:
                    return cost
                for key, (c, r) in directions.items():
                    if key == grid[i][j]:
                        queue.append((i+c, j+r, cost))
                    else:
                        queue.appendleft((i+c, j+r, cost + 1))