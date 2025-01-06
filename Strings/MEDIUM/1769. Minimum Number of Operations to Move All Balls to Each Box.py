# Solution 1: Brute force method.
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = []
        for i in range(n):
            op = 0
            for j in range(n):
                if boxes[j] == '1':
                    op += abs(i - j)
            res.append(op)
        return res
#its a brute force solution i made with the hints given 


#Solution 2: Prefix sum 
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = moves = 0
        res= [0]* len(boxes)
        for i in range(len(boxes)):
            res[i] += balls + moves
            moves = moves + balls
            balls = balls + int(boxes[i])
        #we dont have to make the reverse with the same number of balls and moves so,
        balls = moves = 0
        for i in reversed(range(len(boxes))):
            res[i] += balls + moves
            moves+=balls
            balls+=int(boxes[i])
        return res