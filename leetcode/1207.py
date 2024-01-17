class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mySet = set()
        for v in Counter(arr).values():
            if v in mySet:
                return False
            mySet.add(v)
        return True