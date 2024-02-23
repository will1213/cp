class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        myDict = defaultdict(dict)
        for a in arr1:
            temp = myDict
            s = str(a)
            for c in s:
                if c not in temp:
                    temp[c] = dict()
                temp = temp[c]
        ans = 0
        for b in arr2:
            s = str(b)
            myLen = len(s)
            if myLen < ans:
                continue
            temp = myDict
            index = 0
            while index < myLen and s[index] in temp:
                temp = temp[s[index]]
                index += 1

            ans = max(ans, index)
        return ans