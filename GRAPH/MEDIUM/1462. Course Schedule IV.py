class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for (u, v) in prerequisites:
            adj[u].append(v)
        d=defaultdict(set)
        def dfs(n):
            if n in d:
                return d[n]
            out = set([n])
            for child in adj[n]:
                out.update(dfs(child))
            d[n] = out
            return d[n]
        for (n, _) in queries:
            dfs(n)
        return [v in d[u] for (u, v) in queries]