class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True
        factorDict = defaultdict(set)
        factorToIndexDict = defaultdict(set)
        for i in range(l):
            num = nums[i]
            temp = num
            for j in range(2, int(num ** 0.5)+1):
                if temp % j == 0:
                    factorDict[num].add(j)
                    factorToIndexDict[j].add(i)
                    while temp % j == 0:
                        temp //= j
            if temp > 1:
                factorDict[num].add(temp)
                factorToIndexDict[temp].add(i)
        visitedIndex = set()
        visitedFactor = set()
        q = deque([0])
        visitedIndex.add(0)
        while q:
            index = q.popleft()
            for factor in factorDict[nums[index]]:
                if factor not in visitedFactor:
                    visitedFactor.add(factor)
                    for myIndex in factorToIndexDict[factor]:
                        if myIndex not in visitedIndex:
                            visitedIndex.add(myIndex)
                            q.append(myIndex)
        if len(visitedIndex) == l:
            return True
        return False
