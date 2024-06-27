class Solution:
  def can_construct(self, ransom_note: str, magazine: str) -> bool:
    
    magazine_letters = list(magazine)

    for char in ransom_note:
      if not char in magazine_letters:
        return False
      else:
        magazine_letters.remove(char)
    
    return True


# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
