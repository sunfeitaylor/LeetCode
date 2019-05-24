class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_half(nums, target, i, j, head):
            if i > j:
                return -1

            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if (nums[mid] >= head and (target > nums[mid] or target < head)) or (nums[mid] < target < head):
                return search_half(nums, target, mid + 1, j, head)
            else:
                return search_half(nums, target, i, mid - 1, head)

        if not nums:
            return -1
        return search_half(nums, target, 0, len(nums) - 1, nums[0])


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return i if nums[i] == target else -1
