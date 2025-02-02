# solution with o(n) complexity:
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1: 
                return False
        return True
    
# solution with o(n^2) complexity:
class Solution:
    def check(self, nums: List[int]) -> bool:
        sortedarr = sorted(nums)
        def rotatearr(arr, k):
            k = k % len(arr)  # In case k is greater than the length of the array
            return arr[-k:] + arr[:-k]
        for i in range(len(nums)):
            x = rotatearr(nums,i)
            if x == sortedarr:
                return True
        return False
    
# not optimal but correct  one:
class Solution:
    def check(self, nums: List[int]) -> bool:
        sortedarr = sorted(nums)
        def rotatearr(arr,k):
            d = deque(arr)
            d.rotate(k)
            return list(d)
        for i in range(len(nums)):
            x = rotatearr(nums,i)
            if x == sortedarr:
                return True
        return False


