class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        return max(map.keys(), key=lambda x: map[x])


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        current = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                current = nums[i]
            if current == nums[i]:
                count += 1
            else:
                count -= 1
        return current
