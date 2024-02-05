class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        temp = []
        for i in range(len(nums)):
            if len(temp) < 3:
                if not temp or nums[i] - min(temp) <= k:
                    temp.append(nums[i])
                else:
                    return []
            if len(temp) == 3:
                ans.append(temp)
                temp = []
        return ans