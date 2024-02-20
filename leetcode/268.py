class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        mySum = 0
        for i in range(n+1):
            mySum += i
        return mySum - sum(nums)