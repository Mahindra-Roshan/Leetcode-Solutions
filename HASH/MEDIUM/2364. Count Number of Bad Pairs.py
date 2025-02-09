class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        goodnum = 0
        difference = defaultdict(int)
        for i in range(n):
            diff = nums[i]-i
            goodnum+=difference[diff]
            difference[diff]+=1
        totpair = n*(n-1)//2
        badnum = totpair - goodnum
        return badnum



        