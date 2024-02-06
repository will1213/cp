class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        myDict = defaultdict(int)
        l = len(nums)
        temp = [0] * l
        start = 0
        ans = 0
        for i in range(l-1, -1, -1):
            start += nums[i]
            temp[i] = start
        
        def helper(index, cur):
            if (index,cur) in myDict:
                return myDict[(index, cur)]
            if index < l:
                if (cur - temp[index] <= target) or (cur + temp[index] >= target):
                    a = helper(index+1, cur+nums[index])
                    b = helper(index+1, cur-nums[index])
                    myDict[(index, cur)] = a+b
                    return a+b
                else:
                    return 0
            else:
                if cur == target:
                    return 1
            return 0
        return helper(0, 0)