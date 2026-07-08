# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

# Example 1:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

# Example 2:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

# Example 3:
# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here is the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.




# Brute Force Approach:
# Time Complexity: O(n * (max(bloomDay) - min(bloomDay))) - We are iterating through the entire array and for each day we are checking if it is possible to make m bouquets.
# Space Complexity: O(1) - We are not using any extra space.
from git import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        total_flowers = m*k
        if total_flowers > len(bloomDay):
            return -1
        
        low = min(bloomDay)
        high = max(bloomDay)


        for day in range (low, high + 1):
            if self.is_possible(bloomDay, day, m , k):
                return day
        return -1
        
    
    def is_possible(self, bloom_days, day, m, k):
        count = 0
        bouquets = 0

        for bloom in bloom_days:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
        return bouquets >= m
    





# Optimized Approach:
# Time Complexity: O(n * log(max(bloomDay) - min(bloomDay))) - We are using binary search to find the minimum number of days required to make m bouquets. For each mid value, we are checking if it is possible to make m bouquets.
# Space Complexity: O(1) - We are not using any extra space.
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        total_flowers = m*k
        if total_flowers > len(bloomDay):
            return -1
        
        answer = -1
        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = (low+high)//2
            if self.is_possible(bloomDay, mid, m, k):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer

    
    def is_possible(self, bloom_days, day, m, k):
        count = 0
        bouquets = 0

        for bloom in bloom_days:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
        return bouquets >= m
