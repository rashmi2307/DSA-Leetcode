# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.




class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for char in s:
            if char != " ":
                word += char
            elif word:
                words.append(word)
                word = ""
        if word:
            words.append(word)

        words.reverse()

        return " ".join(words)







# Optimal Approach:
# 1. Initialize an empty string result to store the reversed words.
# 2. Use a pointer to traverse the input string from the end to the beginning.
# 3. Skip any trailing spaces by moving the pointer backward until a non-space character is found.
# 4. Identify the end of the current word by storing the pointer's position.
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        pointer = len(s)-1
        while pointer >= 0:
            while pointer >= 0 and s[pointer] == " ":
                pointer -= 1
            if pointer < 0:
                break
            end = pointer

            while pointer >= 0 and s[pointer] != " ":
                pointer -= 1
            
            word = s[pointer+1:end+1]

            if result != "":
                result += " "

            result += word

        return result
       