class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for u,v in edges:
            u, v = u-1, v-1
            g[u].add(v)
            g[v].add(u)

        ans = defaultdict(lambda: float('-inf'))
        for u in range(n):
            q, visited, steps = [u], set([u]), 0
            while q:
                steps += 1
                q1 = set()
                for u in q:
                    for v in g[u]:
                        if v in q:
                            return -1
                        if v not in visited:
                            q1.add(v)
                            visited.add(v)
                q = q1
            
            k = min(visited)
            ans[k] = max(ans[k], steps)

        return sum(ans.values())