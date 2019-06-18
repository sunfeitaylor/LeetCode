import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = self.partition(nums, i, j)
            if mid > len(nums) - k:
                j = mid - 1
            elif mid < len(nums) - k:
                i = mid + 1
            else:
                return nums[mid]
        return -1

    def partition(self, nums, left, right):
        i = left
        j = right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1
            while i < j and nums[i] <= nums[left]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[i] = nums[i], nums[left]
        return i


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
