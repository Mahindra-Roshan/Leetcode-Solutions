#This is the optimal code for the given problem statement.

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        if len(nums1)%2:
            for x in nums2:
                i^=x
        if len(nums2)%2:
            for x in nums1:
                j^=x
        return i^j


#the code that gave me the memory limit exceeded error,

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = []
        for i in nums1:
            for j in nums2:
                nums3.append(i ^ j)
        res = 0
        for k in nums3:
            res ^= k
        
        return res
    
# so after i've tried i made this one but still the same error occured,
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i in nums1:
            for j in nums2:
                res^=(i ^ j)
        return res