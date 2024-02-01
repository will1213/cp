class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        myDict = defaultdict(list)
        time = defaultdict(int)
        for t in times:
            myDict[t[0]].append((t[1], t[2]))
        visited = set()
        q = deque([[0, k]])
        while q:
            temp = q.popleft()
            visited.add(temp[1])
            if temp[1] in myDict:
                for myTuple in myDict[temp[1]]:
                    if myTuple[0] not in visited:
                        bisect.insort(q, [temp[0] + myTuple[1], myTuple[0]])
                        if myTuple[0] in time:
                            time[myTuple[0]] = min(time[myTuple[0]], temp[0] + myTuple[1])
                        else:
                            time[myTuple[0]] = temp[0] + myTuple[1]
        if len(visited) != n:
            return -1
        return max(time.values())
