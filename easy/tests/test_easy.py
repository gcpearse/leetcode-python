from two_sum import two_sum
from palindrome_number import is_palindrome


def test_two_sum():
  assert two_sum([2, 7, 11, 15], 9) == [0, 1]
  assert two_sum([3, 2, 4], 6) == [1, 2]
  assert two_sum([3, 3], 6) == [0, 1]


def test_is_palindrome():
  assert is_palindrome(121) == True
  assert is_palindrome(-121) == False
  assert is_palindrome(10) == False
