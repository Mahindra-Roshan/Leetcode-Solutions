class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        sumx = 0
        for i in derived:
            sumx^=i
        if sumx ==0:
            return True
        else:
            return False