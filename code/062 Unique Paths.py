class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m] * n
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m] * n
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
