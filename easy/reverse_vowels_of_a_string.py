class Solution:
  def reverse_vowels(self, s: str) -> str:

    chars = list(s)
    
    left = 0
    right = len(chars) - 1

    vowels = set("aeiouAEIOU")
    
    while left < right:
      if not chars[left] in vowels:
        left += 1

      if not chars[right] in vowels:
        right -= 1

      if chars[left] in vowels and chars[right] in vowels:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
      
    return "".join(chars)


# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "hello"
# Output: "holle"

# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
