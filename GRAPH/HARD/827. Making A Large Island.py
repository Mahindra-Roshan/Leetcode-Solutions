class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = [i for i in range(n * n)]
        sizes = [1] * (n * n)

        def find(x):
            while x != uf[x]:
                x = uf[x]
                uf[x] = uf[uf[x]]
            return x

        def connect(a, b):
            a, b = find(a), find(b)
            if a == b: return
            if sizes[a] > sizes[b]:
                uf[b] = uf[a]
                sizes[a] += sizes[b]
            else:
                uf[a] = uf[b]
                sizes[b] += sizes[a]

        def inside(i, j):
            return 0 <= i < n and 0 <= j < n

        for i in range(n):
            for j in range(n):
                if not grid[i][j]: continue
                for ni, nj in ((i + 1, j), (i, j + 1)):
                    if inside(ni, nj) and grid[ni][nj]:
                        connect(i * n + j, ni * n + nj)
        
        res = max(sizes)
        for i in range(n):
            for j in range(n):
                if grid[i][j]: continue
                curr = 1
                for x in {find(ni * n + nj) 
                    for ni, nj in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1))
                    if inside(ni, nj) and grid[ni][nj]}:
                    curr += sizes[x]
                res = max(res, curr)
        return res