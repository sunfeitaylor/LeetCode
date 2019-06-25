class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        l = 1
        r = 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i] *= l
            l *= nums[i]
            res[j] *= r
            r *= nums[j]
        return res
