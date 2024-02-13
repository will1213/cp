class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        p1 = 0
        p2 = len(height)-1
        while p1 < p2:
            ans = max(ans, (p2-p1) * min(height[p1], height[p2]))
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        return ans