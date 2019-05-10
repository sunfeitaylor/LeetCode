from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            if map.get(num) is not None:
                return [map.get(num), index]
            map[target - num] = index
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solute = Solution()
    print(solute.twoSum(nums=nums, target=target))
