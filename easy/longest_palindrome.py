from collections import Counter


class Solution:
  def longest_palindrome(self, s: str) -> int:
    
    tally = Counter(s)
    length = 0
    hasOdds = False

    for value in tally:
      if tally[value] % 2 == 0:
        length += tally[value]
      else:
        length += tally[value] - 1
        hasOdds = True

    return length + 1 if hasOdds == True else length


# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
