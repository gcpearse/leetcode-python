from two_sum import two_sum
from palindrome_number import is_palindrome
from roman_to_integer import roman_to_int
from longest_common_prefix import longest_common_prefix
from valid_parentheses import is_valid
from find_the_index_of_the_first_occurrence_in_a_string import str_str
from search_input_position import search_insert
from length_of_last_word import length_of_last_word
from plus_one import plus_one
from best_time_to_buy_and_sell_stock import max_profit
from valid_palindrome import is_valid_palindrome
from single_number import single_number
from excel_sheet_column_title import convert_to_title
from majority_element import majority_element
from excel_sheet_column_number import title_to_number
from contains_duplicate import contains_duplicate
from power_of_two import is_power_of_two
from valid_anagram import is_anagram


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


def test_longest_common_prefix():
  assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
  assert longest_common_prefix(["dog", "racecar", "car"]) == ""
  assert longest_common_prefix(["cir", "car"]) == "c"


def test_is_valid():
  assert is_valid("()") == True
  assert is_valid("()[]{}") == True
  assert is_valid("(]") == False
  assert is_valid("]") == False
  assert is_valid("){") == False
  assert is_valid("([}}])") == False


def test_str_str():
  assert str_str("sadbutsad", "sad") == 0
  assert str_str("leetcode", "leeto") == -1


def test_search_insert():
  assert search_insert([1, 3, 5, 6], 5) == 2
  assert search_insert([1, 3, 5, 6], 2) == 1
  assert search_insert([1, 3, 5, 6], 7) == 4
  assert search_insert([1], 1) == 0


def test_length_of_last_word():
  assert length_of_last_word("Hello World") == 5
  assert length_of_last_word("   fly me   to   the moon  ") == 4
  assert length_of_last_word("luffy is still joyboy") == 6
  assert length_of_last_word("a") == 1


def test_plus_one():
  assert plus_one([1, 2, 3]) == [1, 2, 4]
  assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
  assert plus_one([9]) == [1, 0]


def test_max_profit():
  assert max_profit([7, 1, 5, 3, 6, 4]) == 5
  assert max_profit([7, 6, 4, 3, 1]) == 0


def test_is_valid_palindrome():
  assert is_valid_palindrome("A man, a plan, a canal: Panama") == True
  assert is_valid_palindrome("race a car") == False
  assert is_valid_palindrome(" ") == True
  assert is_valid_palindrome("ab_a") == True


def test_single_number():
  assert single_number([2, 2, 1]) == 1
  assert single_number([4, 1, 2, 1, 2]) == 4
  assert single_number([1]) == 1


def test_convert_to_title():
  assert convert_to_title(1) == "A"
  assert convert_to_title(28) == "AB"
  assert convert_to_title(701) == "ZY"


def test_majority_element():
  assert majority_element([3, 2, 3]) == 3
  assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_title_to_number():
  assert title_to_number("A") == 1
  assert title_to_number("AB") == 28
  assert title_to_number("ZY") == 701


def test_contains_duplicate():
  assert contains_duplicate([1, 2, 3, 1]) == True
  assert contains_duplicate([1, 2, 3, 4]) == False
  assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


def test_is_power_of_two():
  assert is_power_of_two(1) == True
  assert is_power_of_two(16) == True
  assert is_power_of_two(3) == False


def test_is_anagram():
  assert is_anagram("anagram", "nagaram") == True
  assert is_anagram("rat", "car") == False
