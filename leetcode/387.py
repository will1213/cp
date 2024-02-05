class Solution:
    def firstUniqChar(self, s: str) -> int:
        good = set()
        noGood = set()
        for i in range(len(s)):
            if s[i] in noGood:
                continue
            elif s[i] in good:
                good.remove(s[i])
                noGood.add(s[i])
            else:
                good.add(s[i])
        for i in range(len(s)):
            if s[i] in good:
                return i
        return -1