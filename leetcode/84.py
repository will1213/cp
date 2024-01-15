class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        levels = []
        indexes = []
        for i in range(len(heights)):
            prev = None
            while levels and heights[i] <= levels[-1]:
                h = levels.pop()
                prev = indexes.pop()
                ans = max(ans, h * (i-prev))
            levels.append(heights[i])
            if prev != None:
                indexes.append(prev)
            else:
                indexes.append(i)      
        for j in range(len(levels)):
            ans = max(ans, levels[j] * (len(heights)-indexes[j]))
        return ans