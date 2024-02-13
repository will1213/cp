class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        lc = len(coins)
        dp = [[0] * (amount+1) for _ in range(lc+1)]
        for i in range(1, lc+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[lc][amount]