import math


class Solution:
  def majority_element(self, nums: list[int]) -> int:
    
    if len(nums) == 1:
      return nums[0]
    
    return sorted(nums)[math.floor(len(nums) / 2)]


# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3, 2, 3]
# Output: 3

# Example 2:

# Input: nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2
