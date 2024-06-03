def longest_common_prefix(strs: list[str]) -> str:

  prefix = ""

  for i in range(len(strs)):
    if all(str[i] == strs[0][i] for str in strs):
      prefix += strs[0][i]
    else:
      break

  return prefix


# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
