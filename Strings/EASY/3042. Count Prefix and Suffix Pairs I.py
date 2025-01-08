#its a brute force solution and not that efficient, if there exist any effiecint one please let me know and thanks for visiting

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                l = len(w1)
                if w1 == w2[:l] and w1 == w2[-l:]:
                    count += 1
        return count

