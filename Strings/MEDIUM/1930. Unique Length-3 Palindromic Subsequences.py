#1930. Unique Length-3 Palindromic Subsequences
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for mid in range(len(s)):
            right[s[mid]]-=1
            if right[s[mid]] == 0:
                right.pop(s[mid])
            for c in left:
                if c in right:
                    res.add(c+s[mid]+c)
        
            left.add(s[mid])
        return len(res)