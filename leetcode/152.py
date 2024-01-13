class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = []
        curSum = 0
        ans = 0
        for num in nums:
            if num == 0:
                if curSum < 0 and curSum != dp[0]:
                    ans = max(curSum//dp[0], ans)
                else:
                    if curSum:
                        ans = max(curSum, ans)
                    else:
                        ans = max(ans, 0)
                curSum = 0
                dp = []
            elif num < 0:
                if curSum:
                    curSum *= num
                else:
                    curSum = num
                dp.append(curSum)
                ans = max(curSum, ans)
            else:
                if curSum:
                    curSum *= num
                else:
                    curSum = num
                ans = max(curSum,ans,num)
        if curSum < 0 and curSum != dp[0]:
             ans = max(curSum//dp[0], ans)
        return ans
        
