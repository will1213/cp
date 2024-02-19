class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        roomHeap = []
        timeHeap = []
        # Room
        # num, lastusedTime

        # time
        # endTime, roomNum
        ans = 0
        for i in range(n):
            heapq.heappush(roomHeap, [i, 0])
        roomCount = defaultdict(int)
        for meeting in meetings:
            while timeHeap and timeHeap[0][0] <= meeting[0]:
                time = heapq.heappop(timeHeap)
                heapq.heappush(roomHeap, [time[1], time[0]])
            if roomHeap:
                room = heapq.heappop(roomHeap)
                roomCount[room[0]] += 1
                if roomCount[room[0]] > roomCount[ans]:
                    ans = room[0]
                elif roomCount[room[0]] == roomCount[ans]:
                    ans = min(room[0], ans)
                heapq.heappush(timeHeap, [meeting[1]-meeting[0]+max(room[1], meeting[0]), room[0]])
            else:
                while timeHeap:
                    time = heapq.heappop(timeHeap)
                    heapq.heappush(roomHeap, [time[1], time[0]])
                    if time[0] >= meeting[0]:
                        while timeHeap and timeHeap[0][0] == time[0]:
                            temp = heapq.heappop(timeHeap)
                            heapq.heappush(roomHeap, [temp[1], temp[0]])
                        room = heapq.heappop(roomHeap)
                        roomNum = room[0]
                        roomCount[roomNum] += 1
                        if roomCount[roomNum] > roomCount[ans]:
                            ans = roomNum
                        elif roomCount[roomNum] == roomCount[ans]:
                            ans = min(roomNum, ans)
                        heapq.heappush(timeHeap, [max(room[1], meeting[0]) + meeting[1] - meeting[0], roomNum])
                        break        
        return ans
                    