class Solution:
  def word_pattern(self, pattern: str, s: str) -> bool:

    words = s.split(" ")

    if len(pattern) != len(words):
      return False
    
    pairs = {}

    for i in range(len(pattern)):

      if pattern[i] not in pairs.keys():

        if words[i] not in pairs.values():
          pairs[pattern[i]] = words[i]
        else:
          return False

      elif pairs[pattern[i]] != words[i]:
        return False

    return True


# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
