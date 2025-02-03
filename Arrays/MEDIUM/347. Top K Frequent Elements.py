class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        sorting = sorted(d.items(),key = lambda x : x[1],reverse = True)
        return [num for num,freq in sorting[:k]]