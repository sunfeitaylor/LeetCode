# This is a bad attempt, I used 2 dict: one to record the sum, and one to record the duplicates of the nums.
# In this method, I didn't sort the nums. So it makes the solution too complex.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        map_ = {0 - nums[0] - nums[1]: [[nums[0], nums[1]]]}
        map_duplicate = {nums[0]: 1}
        count = map_duplicate.setdefault(nums[1], 0)
        map_duplicate[nums[1]] = count + 1
        for i in range(2, len(nums)):
            count = map_duplicate.setdefault(nums[i], 0)
            map_duplicate[nums[i]] = count + 1
            if map_duplicate[nums[i]] == 3 and nums[i] == 0:
                res.append([0, 0, 0])
                continue
            if map_duplicate[nums[i]] == 2:
                if map_.get(nums[i]) and True in [nums[i] in x for x in map_.get(nums[i])]:
                    res.append([nums[i], nums[i], -2 * nums[i]])
                map_.setdefault(0 - nums[i] - nums[i], []).append([nums[i], nums[i]])
                continue
            if map_duplicate[nums[i]] == 1:
                if map_.get(nums[i]):
                    for x in map_.get(nums[i]):
                        x = x.copy()
                        x.append(nums[i])
                        res.append(x)
                for j in range(i):
                    if [nums[i], nums[j]] not in map_.setdefault(0 - nums[i] - nums[j], []) \
                            and [nums[j], nums[i]] not in map_.setdefault(0 - nums[i] - nums[j], []):
                        map_.setdefault(0 - nums[i] - nums[j], []).append([nums[i], nums[j]])
        return res


# With sort() used, things are getting better.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if nums[i] > 0:
                # Sum of 3 positive must be greater than 0.
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


# With dict and set being used, it can be faster.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[: -2]):
            if nums[i] > 0:
                # Sum of 3 positive must be greater than 0.
                break
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return list(res)
