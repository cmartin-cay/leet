"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
 container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        areas: list[int] = []
        start: int = 0
        stop: int = len(height) - 1
        gap: int = len(height) - 1

        while start < stop:
            area: int = min(height[start], height[stop]) * gap
            areas.append(area)
            if height[start] < height[stop]:
                start += 1
            else:
                stop -= 1
            gap -= 1
        return max(areas)


print(Solution().maxArea([1, 1]))
