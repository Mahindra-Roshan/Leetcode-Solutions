class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                number = nums[i]*nums[j]
                if number not in map:
                    map[number] = 0
                map[number]+=1
        count = 0
        for i in map.values():
            if i >= 2:
                count+= (i*(i-1)//2)*8
        return count


        