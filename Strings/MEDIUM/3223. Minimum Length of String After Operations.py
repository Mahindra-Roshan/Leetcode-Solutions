class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] +=1
        length = 0
        for j in d.values():
            if j%2:
                length +=1
            else:
                length += 2
        return length

        # we cann write the counting part in a single line as,, but for easy understanding i left it as it is.
        #return sum(1 if j%2 else 2 for j in d.values())

