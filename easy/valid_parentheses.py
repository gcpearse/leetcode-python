class Solution:
  def is_valid(self, s: str) -> bool:

    pairs = {
      "(": ")",
      "[": "]",
      "{": "}"
    }

    stack = []

    for char in s:
      if char in pairs.keys():
        stack.append(char)
      elif len(stack) > 0 and pairs[stack[-1]] == char:
        stack.pop()
      else:
        return False

    return len(stack) == 0


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false
