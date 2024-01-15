class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        index = []
        ans = 0
        for i in range(len(height)):
            h = height[i]
            prev = 0
            while stack and stack[-1] <= h:
                ans += (stack[-1]-prev) * (i - index[-1]-1)
                prev = stack.pop()
                index.pop()
            if stack and stack[-1] > h:
                ans += (h-prev) * (i - index[-1]-1)
            stack.append(h)
            index.append(i)
        return ans