class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        return self.spiralOrderOnce(matrix, res)

    def spiralOrderOnce(self, matrix, res):
        if (not matrix) or (not matrix[0]):
            return res
        elif len(matrix) == 1:
            res += matrix[0]
            return res
        m = len(matrix)
        res += matrix.pop(0)
        i = 0
        while i < m - 2:
            res.append(matrix[i].pop())
            i += 1
        res += reversed(matrix.pop())
        if matrix and matrix[-1]:
            i = m - 3
            while i >= 0:
                res.append(matrix[i].pop(0))
                i -= 1
        else:
            return res
        return self.spiralOrderOnce(matrix, res)
