class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        lockeds = []
        unlockeds = []
        for i in range(len(s)):
            if locked[i]== "0":
                unlockeds.append(i)
            elif s[i] == "(":
                lockeds.append(i)
            else:
                if lockeds:
                    lockeds.pop()
                elif unlockeds:
                    unlockeds.pop()
                else:
                    return False
        while lockeds and  unlockeds and lockeds[-1] < unlockeds[-1]:
            lockeds.pop()
            unlockeds.pop()
        if lockeds:
            return False
        return True if len(unlockeds)%2 == 0 else False