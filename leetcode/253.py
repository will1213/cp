def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x.start)
    count = 0
    ans = 0
    stack = deque()
    for i in intervals:
        while stack and stack[0] <= i[0]:
            stack.popleft()
            count -= 1
        count += 1
        bisect.insort(stack, i[1])
        ans = max(ans, count)
    return ans