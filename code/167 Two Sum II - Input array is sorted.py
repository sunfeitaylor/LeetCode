# map
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for idx, num in enumerate(numbers):
            if num in map:
                return [map[num] + 1, idx + 1]
            map[target - num] = idx


# two-pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            tot = numbers[l] + numbers[r]
            if tot == target:
                return [l + 1, r + 1]
            elif tot < target:
                l += 1
            else:
                r -= 1
