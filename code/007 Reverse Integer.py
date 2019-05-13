# solution without convert int to str
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        res, x = 0, abs(x)
        while x:
            pop = x % 10
            x = x // 10
            res = res * 10 + pop
            if res > 2 ** 31 - 1 or res < - 2 ** 31:
                res = 0
        return sign * res


# solution with convert int to str
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        res = int(str(abs(x))[::-1]) * sign
        return res if -2 ** 31 < res < 2 ** 31 - 1 else 0
