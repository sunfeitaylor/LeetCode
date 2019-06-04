class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, 2 ** n):
            res.append(res[-1] ^ (i & -i))
        return res


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ i >> 1 for i in range(1 << n)]
