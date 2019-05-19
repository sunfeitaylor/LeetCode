class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        res = nums[0] + nums[1] + nums[-1]
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total
                elif total < target:
                    if abs(total - target) < abs(res - target):
                        res = total
                    l += 1
                else:
                    if abs(total - target) < abs(res - target):
                        res = total
                    r -= 1
        return res
