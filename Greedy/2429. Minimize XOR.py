class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ones = bin(num2).count('1')
        res= 0
        for i in range(31, -1, -1):
            if ones == 0:
                break
            if num1 & (1 << i): 
                res |= (1 << i) 
                ones -= 1
        for i in range(32):
            if ones == 0:
                break
            if not (res & (1 << i)): 
                res |= (1 << i)  
                ones -= 1
        return res
