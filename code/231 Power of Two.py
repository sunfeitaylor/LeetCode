class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 2:
            return False
        else:
            return self.isPowerOfTwo(n / 2)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        mi = 2
        while mi <= n:
            if mi == n:
                return True
            else:
                mi *= 2
        return False


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & n - 1 == 0
