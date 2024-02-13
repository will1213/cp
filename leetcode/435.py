class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        prev = None
        ans = 0
        for i in intervals:
            if prev and i[0] < prev[1]:
                if i[1] < prev[1]:
                    prev = i
                ans += 1
            else:
                prev = i
        return ans