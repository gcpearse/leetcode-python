def convert_to_title(column_number: int) -> str:
  
  number = column_number
  title = ""

  while number > 0:

    remainder = number % 26
    number -= remainder

    if remainder:
      title += chr(int(remainder) + 64)
      number /= 26
    else:
      title += "Z"
      number /= 26
      number -= 1

  return title[::-1]


# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

# Input: columnNumber = 1
# Output: "A"

# Example 2:

# Input: columnNumber = 28
# Output: "AB"

# Example 3:

# Input: columnNumber = 701
# Output: "ZY"
