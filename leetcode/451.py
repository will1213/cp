class Solution:
    def frequencySort(self, s: str) -> str:
        temp = []
        count = Counter(s)
        for k, v in count.items():
            heapq.heappush(temp, (-v, k))
        ans = ''
        while temp:
            t = heapq.heappop(temp)
            ans += t[1] * -t[0]
        return ans