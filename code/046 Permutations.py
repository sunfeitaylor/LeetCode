class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums: List[int], path: List[int], res: List[List[int]]):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0, nums, res)
        return res

    def backtrack(self, first, nums, res):
        if first == len(nums):
            res.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            self.backtrack(first + 1, nums, res)
            nums[first], nums[i] = nums[i], nums[first]
