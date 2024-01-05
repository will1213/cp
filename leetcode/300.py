class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp.values())