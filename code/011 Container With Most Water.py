# The idea is : to compute area, if height[i] < height[j],
# then the expression min(height[i], height[j]) will always lead to at maximum height[i] for all other j(i being fixed),
# hence no point checking them.
# For example, if height[0] < height[6], then area = height[0] * (6 - 0),
# which is larger than the pairs like (0, 1), (0, 2), (0, 3)... since area(0, 3) = height[0] * (3 - 0)
# Similarly when height[i] > height[j] then all the other i's can be ignored for that particular j.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while j != i:
            if height[i] > height[j]:
                res = max(res, height[j] * (j - i))
                j -= 1
            else:
                res = max(res, height[i] * (j - i))
                i += 1
        return res
