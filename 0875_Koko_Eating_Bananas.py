# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23




# Brute Force Approach:
# Time Complexity: O(n * max(piles)) - We are iterating through the entire array and for each element we are calculating the total hours required to eat all the bananas.
# Space Complexity: O(1) - We are not using any extra space.
from ast import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxVal = max(piles)
        for i in range (1, maxVal+1):
            hours = self.calculateTotalHours(piles,i)
            if hours <= h:
                return i
        return maxVal


    def calculateTotalHours(self, piles: List[int], hourly: int) -> int:
        totalHours = 0
        for pile in piles:
            totalHours += math.ceil(pile/hourly)
        return totalHours
