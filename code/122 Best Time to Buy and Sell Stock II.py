class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        i = 0
        for j in range(len(prices) - 1):
            if prices[j] < prices[i]:
                i = j
            elif prices[j + 1] < prices[j]:
                best += prices[j] - prices[i]
                i = j
        if prices[-1] > prices[i]:
            best += prices[-1] - prices[i]
        return best


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                best += prices[i + 1] - prices[i]
        return best
