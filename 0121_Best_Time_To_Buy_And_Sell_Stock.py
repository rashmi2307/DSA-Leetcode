# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.



# Brute Force Approach
# Time Complexity: O(n^2) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the maximum
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        for i in range (n):
            for j in range (i+1, n):
                profit = prices[j] - prices[i]
                maxprofit = max(profit, maxprofit)
        return maxprofit


# Optimal Approach
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we are using only constant space to store the maximum
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            if prices[i] - mini > maxprofit:
                maxprofit = prices[i] - mini
        return maxprofit