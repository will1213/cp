class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k == 0 or l == 1 or k == l:
            return
        r = k % l
        temp = nums[-r:]
        temp2 = nums[:-r]
        for i in range(l):
            if i < r:
                nums[i] = temp[i]
            else:
                nums[i] = temp2[i-r]
        return 