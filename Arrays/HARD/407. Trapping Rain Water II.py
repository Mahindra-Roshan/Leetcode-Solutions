
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        rows =len(heightMap)
        cols = len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        minheap = []
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heappush(minheap, (heightMap[r][c], r, c))
                    visited[r][c] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        trappedwater = 0
        while minheap:
            height, x, y = heappop(minheap)
            for dx,dy in directions:
                nx =x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:#visited or not
                    visited[nx][ny] = True
                    trappedwater += max(0, height - heightMap[nx][ny])
                    heappush(minheap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return trappedwater
    
    # i'm gonna give a brief explanation here to understand how my code works.
    #initially we are checking if the height exist because if there is no height exist we cannot store the water and hence the water stored is 0
    #so now we are going to initialise a min heap to find the minimum height and to compare with the neighbouring heights.
    #initially im making every nodes as not visited so that when the columns are visited it gets updated here.
    #After the minheap is populated with the given input, now we have to check for the amount of water being trapped
    #So i,ve used a while loop and the hieght ,x,y are taken from the minheap that we previously populated. then we calculate the nx and ny where dy here is the direction to go either left right down up etc
    # after that we check if the current col is visited or not if not visited we traverse through tjat and make that as visited as we seen previouslu
    # to check for the trapped water we find the maximum of  0 and height - heightmap of current nx and ny values calculated.
    # then we pust the maximum to the min heap and return the trapped water being calculated so far.

#partwise explanation:

# 1. first, check if the height map exists. if it doesnt return 0 because no water can be trapped
# 2. Initialize a minheap to store boundary cells. These act as the initial boundaries for trapping water
#    also mark all cells as unvisited in a `visited` matrix
# 3. Add all boundary cells to the minheap and mark them as visited.
# 4. Start processing the minheap. for each cell smallest height is processed first
#    a.extract the cell's height and coordinates.
#    b.traverse its neighbors (up, down, left, right).
#    c.if the neighbor hasn’t been visited:
#       - mark it as visited.
#       - calculate trapped water as max(0, height - heightMap[nx][ny])
#       - aadd the neighbor to the heap with the updated height max(height, heightMap[nx][ny]
# 5. continue processing the heap until all cells are visited.
# 6. return the total trapped water.

    
