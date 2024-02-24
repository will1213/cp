class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        myDict = defaultdict(list)
        nodeList = [math.inf] * n
        nodeList[src] = 0
        for f in flights:
            myDict[f[0]].append((f[1], f[2]))

        q = deque([(src,0)])
        stop = 0
        nextQ = deque()
        while q and stop <= k:
            node, price = q.popleft()
            for neighbor, addPrice in myDict[node]:
                if price+addPrice < nodeList[neighbor]:
                    nextQ.append((neighbor, price+addPrice))
                    nodeList[neighbor] = price+addPrice
            if not q:
                q = nextQ
                nextQ = deque()
                stop += 1
        return nodeList[dst] if nodeList[dst] != math.inf else -1