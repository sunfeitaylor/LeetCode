# Bit Manipulation
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        res = []
        for i in range(2 ** m):
            binStr = ''
            while i > 0:
                binStr = str(i % 2) + binStr
                i = i // 2
            binStr = (m - len(binStr)) * '0' + binStr
            subset = []
            for j in range(len(binStr)):
                if binStr[j] == '1':
                    subset.append(nums[j])
            res.append(subset)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res


# DFS recursively
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)


# Iteratively
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res
