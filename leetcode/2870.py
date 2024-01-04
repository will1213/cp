class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for k, v in count.items():
            if v == 1:
                return -1
            if v % 3 in [0, 2]:
                ans += math.ceil(v / 3)
            else:
                ans += v // 3
                ans += 1
        return ans