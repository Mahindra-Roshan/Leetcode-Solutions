class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        rowcounts=[0]*m
        colcounts=[0]*n
        res=0
        arr=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rowcounts[i]+=1
                    colcounts[j]+=1
                    arr.append([i,j])
        for i,j in arr:
            if rowcounts[i]>1 or colcounts[j]>1:
                res+=1
        return res