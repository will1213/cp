class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        cur = 0
        for i in range(len(nums)):
            if i >= 2:
                if cur > nums[i]:
                    ans = max(ans, cur+nums[i])
            cur += nums[i]
        return ans