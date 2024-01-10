class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        def helper(i, cur):
            if i >= n:
                return
            if len(cur) >= 2:
                diff = cur[-1] - cur[-2]
                if nums[i] - cur[-1] == diff:
                    nonlocal ans 
                    ans += 1
                    helper(i+1, copy.deepcopy(cur+[nums[i]]))
                helper(i+1, cur)
            else:
                helper(i+1, copy.deepcopy(cur+[nums[i]]))
                helper(i+1, cur)
        helper(0, [])
        return ans