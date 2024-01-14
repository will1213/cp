class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        i = []
        for index in range(len(s)-len(a)+1):
            if s[index:index+len(a)] == a:
                i.append(index)
        j = []
        for index in range(len(s)-len(b)+1):
            if s[index:index+len(b)] == b:
                j.append(index)
        ans = []
        for myI in i:
            for myJ in j:
                if abs(myI-myJ) <= k:
                    ans.append(myI)
                    break
        return ans