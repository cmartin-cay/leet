"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return common_prefix
            else:
                common_prefix += first[i]
        return common_prefix

print(Solution().longestCommonPrefix(["a"]))