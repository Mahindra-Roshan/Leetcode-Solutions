class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        partlen = len(part)
        for i in s:
            stack.append(i)
            if stack[-partlen:] == list(part):
                for _ in range(partlen):
                    stack.pop()
        return ''.join(stack)
    

#solution2: optimal

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)  # Remove one occurrence at a time
        return s

        