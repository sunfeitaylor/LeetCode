# Solution 1: recursion solution
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        nums = list(range(1, n ** 2 + 1))
        if n % 2:
            # n: odd number
            res.append([nums.pop()])
            return self.generateMatrixOnce(nums, res)
        else:
            # n: even number
            res.append(nums[:-3:-1].copy())
            res.insert(0, nums[-4:-2].copy())
            return self.generateMatrixOnce(nums[:-4], res)

    def generateMatrixOnce(self, nums, res):
        if not nums:
            return res
        m = len(res)
        for i in range(m):
            res[i].insert(0, nums.pop())
        res.append(nums[:-m - 3:-1].copy())
        nums = nums[: -m - 2]
        for i in reversed(range(m)):
            res[i].append(nums.pop())
        res.insert(0, nums[-m - 2:].copy())
        nums = nums[: -m - 2]
        return self.generateMatrixOnce(nums, res)


# Solution 2: Walk the spiral
# Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n.
# Make a right turn when the cell ahead is already non-zero.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            A[i][j] = k + 1
            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A


# Solution 3: Build it inside-out
# Start with the empty matrix, add the numbers in reverse order until we added the number 1.
# Always rotate the matrix clockwise and add a top row:
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res, low = [[n * n]], n * n
        while low > 1:
            low, high = low - len(res), low
            res = [list(range(low, high))] + [list(j) for j in zip(*res[::-1])]
        return res
