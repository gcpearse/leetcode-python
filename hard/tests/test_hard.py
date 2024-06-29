import valid_number


def test_is_number():

  solution = valid_number.Solution()

  assert solution.is_number("0") == True
  assert solution.is_number("e") == False
  assert solution.is_number(".") == False
