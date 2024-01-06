class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        myList = []
        for i in range(len(startTime)):
            myList.append([endTime[i], startTime[i], profit[i]])
        myList.sort()
        dp = [[0,0]]
        def helper(i):
            sTime = myList[i][1]
            eTime = myList[i][0]
            pro = myList[i][2]
            temp = bisect_right(dp, sTime, key=lambda x: x[0])
            if temp >= len(dp):
                prev = dp[-1][1]
                cur = dp[-1][1]
            else:
                if dp[temp][0] > sTime:
                    temp -= 1
                prev = dp[temp][1]
                temp2 = bisect_right(dp, eTime, key = lambda x: x[0])
                if temp2 >= len(dp):
                    cur = dp[-1][1]
                else:
                    if dp[temp2][0] > eTime:
                        temp2 -= 1
                    cur = dp[temp2][1]
            dp.append([eTime, max(prev+pro, cur)])

        for i in range(len(endTime)):
            helper(i)
        return dp[-1][1]