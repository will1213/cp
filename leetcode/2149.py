class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        positiveIndex = 0
        negativeIndex = 1
        for num in nums:
            if num < 0:
                ans[negativeIndex] = num
                negativeIndex += 2
            else:
                ans[positiveIndex] = num
                positiveIndex += 2
        return ans