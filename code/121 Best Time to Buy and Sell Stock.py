class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        i = 0
        for j in range(len(prices)):
            if prices[j] < prices[i]:
                i = j
            elif prices[j] - prices[i] > best:
                best = prices[j] - prices[i]
        return best
