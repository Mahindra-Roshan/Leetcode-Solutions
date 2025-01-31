class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        exlist=[float('inf')] * n
        exlist[src]=0
        for i in range(k+1):
            temp=exlist.copy()
            for s,e,w in flights:
                if exlist[s]==float('inf'):
                    continue
                if exlist[s]+w < temp[e]:
                    temp[e]=exlist[s]+w
            exlist=temp
        return -1 if exlist[dst] == float('inf') else exlist[dst]