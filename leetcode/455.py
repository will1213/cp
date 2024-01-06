class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        si = 0
        gi = 0
        ans = 0
        while si < len(s) and gi < len(g):
            if s[si] >= g[gi]:
                si += 1
                gi += 1 
                ans += 1
            else:
                gi += 1
        return ans