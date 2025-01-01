#Solution 1:

class Solution:
    def maxScore(self, s: str) -> int:
        maximum = 0
        for i in range(1,len(s)):
            countof0 = s[:i].count("0")
            countof1 = s[i:].count("1")
            total = countof1 + countof0
            maximum= max(maximum,total)
        return maximum

# Solution 2:

class Solution:
    def maxScore(self, s: str) -> int:
        maxi = 0
        n = len(s)
        for i in range(1,n):
            countof0 = 0
            countof1 = 0
            left = s[0:i]
            for j in left:
                if j == "0":
                    countof0+=1
            x = n - len(left)
            right = s[i:]
            for k in right:
                if k == "1":
                    countof1 += 1
            total = countof1+countof0
            maxi = max(maxi,total)
        return maxi