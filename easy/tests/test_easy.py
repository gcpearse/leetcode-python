from two_sum import two_sum
from palindrome_number import is_palindrome
from roman_to_integer import roman_to_int


def test_two_sum():
  assert two_sum([2, 7, 11, 15], 9) == [0, 1]
  assert two_sum([3, 2, 4], 6) == [1, 2]
  assert two_sum([3, 3], 6) == [0, 1]


def test_is_palindrome():
  assert is_palindrome(121) == True
  assert is_palindrome(-121) == False
  assert is_palindrome(10) == False


def test_roman_to_int():
  assert roman_to_int("III") == 3
  assert roman_to_int("LVIII") == 58
  assert roman_to_int("MCMXCIV") == 1994
