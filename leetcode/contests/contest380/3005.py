class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        temp = max(cnt.values())
        ans = 0
        for k, v in cnt.items():
            if v == temp:
                ans += temp
        return ans