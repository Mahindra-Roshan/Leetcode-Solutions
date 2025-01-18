class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        sumx = 0
        for i in derived:
            sumx^=i
        return sumx ==0
            