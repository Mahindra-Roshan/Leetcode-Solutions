from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(counter):
            total = 0
            for tile in counter:
                if counter[tile] > 0:
                    total += 1 
                    counter[tile] -= 1 
                    total += dfs(counter)  
                    counter[tile] += 1 
            return total
        
        return dfs(Counter(tiles))
