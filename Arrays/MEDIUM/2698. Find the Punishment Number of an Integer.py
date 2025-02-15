class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(s, t, i):
            if i == len(s):
                return t == 0
            num = 0
            for j in range(i, len(s)):
                num = num * 10 + int(s[j])
                if num > t:
                    break
                if check(s, t - num, j + 1):
                    return True
            return False

        res = 0
        for i in range(1, n + 1):
            sq = i * i
            if check(str(sq), i, 0):
                res += sq
        return res
