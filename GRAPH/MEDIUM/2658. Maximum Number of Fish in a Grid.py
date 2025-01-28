class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or grid[r][c] ==0:
                return 0 #i return 0 if only land exist or all are visistted.

            visited[r][c] = True # i make the water land as starting
            fish_count = grid[r][c]

            for dr, dc in directions: #also calculated the all 4 directions
                fish_count += dfs(r + dr, c + dc)
            return fish_count
            
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        max_fish = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]: #dfs for finding the maximum fish that can be caught.
                    max_fish = max(max_fish, dfs(r, c))
        return max_fish
