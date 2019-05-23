# This solution is bad.
# I misunderstood the description and thought that we must provide a duplicated nums.
# So I tried to del the duplicates locally.
# And the result is bad.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        val = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                val = nums[i]
                i += 1
        return len(nums)


# Double pointer solution.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    solute = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solute.removeDuplicates(nums)
