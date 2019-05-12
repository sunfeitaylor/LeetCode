# dp solution: Time complexity O(N^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        max_len = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(0, n - 1):
            for j in range(i, -1, -1):
                dp[i][j] = s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1])
                if dp[i][j] and max_len < i - j + 1:
                    max_len = i - j + 1
                    result = s[j: i + 1]
        return result


# from middle to two ends solution: Time complexity O(N)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[:: -1]:
            return s

        length = 1

        # for the even case: like 'aabbaa'
        even_medium = 0
        even_left = 0
        for i in range(len(s) - 1):
            if i - even_left >= 0 and s[i - even_left] == s[i + 1]:
                substring = s[i - even_left: i + 2]
                if substring == substring[:: -1]:
                    even_medium = i
                    length = even_left + 2
                    even_left += 2

        # for the odd case: like 'aabaa'
        half = (length + 1) // 2
        odd_medium = 0
        odd_left = (length + 1) // 2
        for j in range(half, len(s) - half):
            if j - odd_left >= 0 and s[j - odd_left] == s[j + half]:
                substring = s[j - odd_left: j + half + 1]
                if substring == substring[:: -1]:
                    odd_medium = j
                    length = odd_left + half + 1
                    odd_left += 2

        if length % 2:
            return s[odd_medium + half + 1 - length: odd_medium + half + 1]
        else:
            return s[even_medium + 2 - length: even_medium + 2]
