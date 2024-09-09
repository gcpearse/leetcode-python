class Solution:
  def find_disappeared_numbers(self, nums: list[int]) -> list[int]:

    unique = set(nums)

    result = []

    for n in range(1, len(nums) + 1):
      if n not in unique:
        result.append(n)

    return result


# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
