class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = Counter(nums)
        row = 0
        while cnt:
            ans.append([])
            temp = set()
            for k in cnt.keys():
                if cnt[k] == 1:
                    temp.add(k)
                else:
                    cnt[k] -= 1
                ans[row].append(k)
            for i in temp:
                del cnt[i]
            row += 1
        return ans
        