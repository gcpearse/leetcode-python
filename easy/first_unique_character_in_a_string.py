from collections import Counter


class Solution:
  def first_uniq_char(self, s: str) -> int:

    tally = Counter(s)

    for char, count in tally.items():
      if count == 1:
        return s.index(char)

    return -1


# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0

# Example 2:

# Input: s = "loveleetcode"
# Output: 2

# Example 3:

# Input: s = "aabb"
# Output: -1
