class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = []
        seen = set()
        count = 0
        for a, b in zip(A, B):
            if a in seen:
                count += 1
            else:
                seen.add(a)
            if b in seen:
                count += 1
            else:
                seen.add(b)
            common.append(count)
        return common
