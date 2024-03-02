class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        middle = bisect.bisect_left(nums, 0)
        ans = []
        l = middle - 1
        r = middle
        leng = len(nums) - 1
        while l >= 0 or r <= leng:
            if l < 0:
                ans.append(nums[r] ** 2)
                r += 1
            elif r > leng:
                ans.append(nums[l] ** 2)
                l -= 1
            else:
                if abs(nums[l]) > nums[r]:
                    ans.append(nums[r] ** 2)
                    r += 1
                else:
                    ans.append(nums[l] ** 2)
                    l -= 1
        return ans