from typing import List


# The first solution is a divide and conquer solution.
# The idea is:
#     1. find the medians of the two lists separately
#     2. according to the medians, remove a constant fraction of elements whose removals do not affect the solution
#     3. go back to 1 and do the recursion
# But still it's not easy to get the right result for the edged cases.
# And here the sorted() function used in the edged cases might not be a good idea.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        def getMedian(nums):
            if not nums:
                return None
            n_nums = len(nums)
            return (nums[n_nums // 2] + nums[n_nums // 2 - (n_nums % 2 == 0)]) / 2

        if m <= 2:
            if n < 4:
                nums1 += nums2
            else:
                nums1 += nums2[n // 2 - 2 + n % 2: n // 2 + 2]
            return getMedian(sorted(nums1))

        med1, med2 = getMedian(nums1), getMedian(nums2)
        idx = int((m - .5) // 2)

        if med1 < med2:
            return self.findMedianSortedArrays(nums1[idx:], nums2[: - idx])
        elif med1 > med2:
            return self.findMedianSortedArrays(nums1[: - idx], nums2[idx:])
        else:
            return med1


# The second solution is an index solution.
# The idea is to find the proper index (i, j) that separates the two arrays apart:
#     1. len(left_part) = len(right_part), which means i + j = m - i + n - j (or: m - i + n - j + 1)
#     2. max(left_part) <= min(right_part)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        i_min, i_max = 0, m
        tot_med = (m + n + 1) // 2
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            # note that j is a function of i
            j = tot_med - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, increase i
                i_min = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too large, decrease i
                i_max = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    solute = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(solute.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solute.findMedianSortedArrays(nums1, nums2))
