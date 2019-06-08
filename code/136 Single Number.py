class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            cache[num] = cache.get(num, 0) + 1
            if cache[num] == 2:
                cache.pop(num)
        return cache.popitem()[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
