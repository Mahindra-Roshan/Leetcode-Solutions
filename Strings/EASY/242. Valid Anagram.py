class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count= {}
        for char in s:
            if char in count:
                count[char] +=1
            else:
                count[char] = 1
        for c in t:
            if c not in count or count[c]==0:
                return False
            count[c]-=1
        return True