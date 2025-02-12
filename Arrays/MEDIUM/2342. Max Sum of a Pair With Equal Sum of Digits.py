class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n= len(nums)
        d = defaultdict(list)
        for i in range(n):
            x  = sum(int(d) for d in str(nums[i]))
            d[x].append(nums[i])
        sortedpairs = sorted(d.items(),key = lambda x:x[1])
        maxsum = -1
        for key in d:
            if len(d[key]) > 1:  
                d[key].sort(reverse=True) 
                maxsum = max(maxsum, d[key][0] + d[key][1])
        
        return maxsum
        

        


            


        