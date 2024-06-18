class Solution:
  def is_anagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):
      return False
    
    return "".join(sorted(s)) == "".join(sorted(t))


# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false
