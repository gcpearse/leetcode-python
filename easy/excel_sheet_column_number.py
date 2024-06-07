def title_to_number(column_title: str) -> int:

  result = 0
  multiplier = 1
  
  for i in range(len(column_title) - 1, -1, -1):
    result += (ord(column_title[i]) - 64) * multiplier
    multiplier *= 26

  return result


# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1

# Example 2:

# Input: columnTitle = "AB"
# Output: 28

# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
