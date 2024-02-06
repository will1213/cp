class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myDict = defaultdict(int)
        p1 = 0
        ans = 0
        myLen = len(s)
        for i in range(myLen):
            myDict[s[i]] += 1
            while (i - p1 +1) - myDict[s[p1]] > k:
                ans = max(ans, i-p1)
                myDict[s[p1]] -= 1
                p1 += 1
        used = set()
        while p1 < myLen:
            if s[p1] not in used:
                l = myLen - p1
                temp = myDict[s[p1]]
                notSame = l-temp
                ans = max(ans, min(myLen, l + (k-notSame)))
                used.add(s[p1])
            p1 += 1
        return ans