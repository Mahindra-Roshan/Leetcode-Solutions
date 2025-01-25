class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        group = []
        numgroup = {}
        for i in sorted(nums):
            if not group or abs(i - group[-1][-1]) > limit:
                group.append(deque())
            group[-1].append(i)
            numgroup[i] = len(group) -1
        res = []
        for n in nums:
            m = numgroup[n]
            res.append(group[m].popleft())
        return res
        