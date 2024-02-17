class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        l = len(heights)
        heap = []
        lheap = 0
        for i in range(1, l):
            if heights[i] > heights[i-1]:
                if lheap == ladders:
                    bricks -= heapq.heappushpop(heap, heights[i] - heights[i-1])
                    if bricks < 0:
                        return i-1
                else:
                    heapq.heappush(heap, heights[i]-heights[i-1])
                    lheap += 1
        return l-1