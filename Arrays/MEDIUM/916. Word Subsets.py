from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maximum = Counter()
        for i in words2:
            maximum |= Counter(i)
        res = []
        for j in words1:
            count = Counter(j)
            if all(count[k]>= maximum[k] for k in maximum):
                res.append(j)
        return res                