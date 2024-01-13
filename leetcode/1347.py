class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = Counter(s)
        ans = 0
        for c in t:
            if c in cnt:
                if cnt[c] == 1:
                    del cnt[c]
                else:
                    cnt[c] -= 1
            else:
                ans += 1
        return ans