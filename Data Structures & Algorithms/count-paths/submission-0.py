class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [1] * n

        for i in range(m-1):
            newDP = [1] * n
            for j in range(n-2, -1, -1):
                newDP[j] = newDP[j+1] + dp[j]
            dp = newDP
        return dp[0]
        