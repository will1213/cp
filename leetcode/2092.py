class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ans = set([0, firstPerson])
        myDict = defaultdict(list)
        for m in meetings: 
            myDict[m[0]].append((m[1], m[2]))
            myDict[m[1]].append((m[0], m[2]))
        q = deque([(0, 0), (firstPerson, 0)])
        personList = [math.inf] * n
        personList[0] = 0
        personList[firstPerson] = 0
        while q:
            l = len(q)
            i = 0
            while i < l:
                person, time = q.popleft()
                personList[person] = min(time, personList[person])
                for meeting in myDict[person]:
                    if meeting[1] >= personList[person]:
                        if personList[meeting[0]] > meeting[1]:
                            q.append((meeting[0], meeting[1]))
                            ans.add(meeting[0])
                i += 1
        return ans
