class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        result = 0
        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]
            if left>=right:
                result+=1
            else:0
        return result
