class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        colors = defaultdict(int)
        balls = defaultdict(int)
        for ball, color in queries:
            if ball in balls:
                prev = balls[ball]
                if prev == color:
                    result.append(len(colors))
                    continue
                colors[prev] -= 1
                if colors[prev] == 0:
                    del colors[prev]
            colors[color] += 1
            balls[ball] = color    
            result.append(len(colors))
        return result    