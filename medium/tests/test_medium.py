import integer_to_roman


def test_int_to_roman():

  solution = integer_to_roman.Solution()

  assert solution.int_to_roman(3749) == "MMMDCCXLIX"
  assert solution.int_to_roman(58) == "LVIII"
  assert solution.int_to_roman(1994) == "MCMXCIV"
