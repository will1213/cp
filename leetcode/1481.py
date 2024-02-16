class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        temp = sorted(count.values())
        l = len(temp)
        for i in temp:
            if i <= k:
                k -= i
                l -= 1
            else:
                break
        return l