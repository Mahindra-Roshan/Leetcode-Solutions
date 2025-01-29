from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty: #we can sayy the cycle is found
                return False
            parent[rootx] = rooty
            return True
        for u,v in edges:
            if u not in parent:
                parent[u]=u
            if v not in parent:
                parent[v]=v
            if not union(u,v):
                return [u,v]

