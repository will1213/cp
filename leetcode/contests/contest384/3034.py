class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-len(pattern)):
            prev = nums[i]
            success = True
            for j in range(len(pattern)):
                cur = nums[i+j+1]
                if pattern[j] == -1:
                    if prev <= cur:
                        success = False
                        break
                elif pattern[j] == 0:
                    if prev != cur:
                        success = False
                        break
                else:
                    if prev >= cur:
                        success = False
                        break
                prev = cur
            if success:
                ans += 1
        return ans