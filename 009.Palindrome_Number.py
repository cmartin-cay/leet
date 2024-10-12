"""Given an integer x, return true if x is a palindrome, and false otherwise."""

"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_list = str(x)
        if num_list == num_list[::-1]:
            return True
        return False


print(Solution().isPalindrome(-121))
