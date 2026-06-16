# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
 
# Constraints:
# -231 <= x <= 231 - 1



class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        if x<0:
            sign = -1
        else: 
            sign = 1
        x = abs(x)
        while x!=0:
            if reverse <214748364:
                reverse = reverse*10 + x%10
                x = x//10
            elif reverse ==214748364 and x%10 <= 7: 
                reverse = reverse*10 + x%10
                x = x//10
            else: 
                return 0
        return sign*reverse