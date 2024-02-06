class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for s in strs:
            myDict[''.join(sorted(s))].append(s)
        return myDict.values()