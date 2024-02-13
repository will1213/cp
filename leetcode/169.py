class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        temp = nums[0]
        count = 0
        for i in range(l):
            if nums[i] != temp:
                if count > (l // 2):
                    return temp
                else:
                    temp = nums[i]
                    count = 0
            count += 1
        return nums[-1]