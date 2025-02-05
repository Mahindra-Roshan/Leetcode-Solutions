class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            # Check if there's at least one duplicate character in s
            return len(set(s)) < len(s)
        
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        if len(diff) == 2:
            # Swap the two mismatched characters and check if they match the goal
            dummy = list(s)
            dummy[diff[0]], dummy[diff[1]] = dummy[diff[1]], dummy[diff[0]]
            return ''.join(dummy) == goal
        
        return False
