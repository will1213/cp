class Solution:
    def jump(self, nums: List[int]) -> int:
        def helper(low, high):
            newLow = high+1
            newHigh = -1
            for i in range(low, high+1):
                newHigh = max(i+nums[i], newHigh)
                if nums[i] and nums[i]+i > high:
                    newLow = min(newLow, nums[i]+i)
            return [newLow, newHigh]
        temp = [0,0]
        ans = 0
        while temp[1] < len(nums)-1:
            ans += 1
            temp = helper(temp[0],temp[1])
        return ans