class Solution:
  def is_power_of_three(self, n: int) -> bool:
    
    i = 0

    while True:
      if 3 ** i <= n:
        if 3 ** i == n:
          return True
      else:
        return False
      i += 1


# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3^x.

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 3^3

# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3^x = 0.

# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3^x = (-1).
