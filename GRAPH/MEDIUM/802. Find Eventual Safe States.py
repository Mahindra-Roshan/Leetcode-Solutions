#solution:1
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n
        def safe(node):
            if state[node] != 0:
                return state[node] == 1 
            state[node] = -1  
            for neighbor in graph[node]:
                if not safe(neighbor):  
                    return False
            state[node] = 1 
            return True
        return [i for i in range(n) if safe(i)]

# solution: 2
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return safe[i]
            safe[i]= True
            return safe[i]
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res