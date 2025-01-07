class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = len(words)
        res = []
        for i in range(l):
            for j in range(l):
                if i != j and words[j].find(words[i])!=-1:
                    res.append(words[i])
                    break
        return res