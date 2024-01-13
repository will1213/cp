class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = defaultdict(bool)
        ans = 0
        for i in range(len(s)):
            dp[(i,i)] = True
            ans += 1
            for j in range(i-1, -1, -1):
                if s[j] == s[i]:
                    if i-j == 1:
                        dp[(j, i)] = True
                        ans += 1
                    else:
                        dp[(j, i)] = dp[(j+1, i-1)]
                        if dp[(j, i)]:
                            ans += 1
        return ans
                        
