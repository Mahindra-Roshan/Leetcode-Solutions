class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        count = Counter(s)
        odd = 0
        for i in count.values():
            if i%2 == 1:
                odd +=1
        return odd <= k
        