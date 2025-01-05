class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        difference =[0]*(len(s)+1)
        for start,end,direct in shifts:
            difference[start] +=1 if direct == 1 else -1
            difference[end +1] -=1 if direct == 1 else -1
        shift = 0
        result = []
        for i in range(len(s)):
            shift += difference[i]
            new = chr((ord(s[i]) - ord('a') +shift) % 26 + ord('a'))
            result.append(new)

        return ''.join(result)
        