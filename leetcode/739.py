class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp = stack.pop()
                ans[temp[1]] = i - temp[1]
            stack.append([t, i])
        return ans