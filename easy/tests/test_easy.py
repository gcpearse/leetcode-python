import two_sum
import palindrome_number
import roman_to_integer
import longest_common_prefix
import valid_parentheses
import find_the_index_of_the_first_occurrence_in_a_string
import search_input_position
import length_of_last_word
import plus_one
import best_time_to_buy_and_sell_stock
import valid_palindrome
import single_number
import excel_sheet_column_title
import majority_element
import excel_sheet_column_number
import contains_duplicate
import power_of_two
import valid_anagram
import add_digits
import missing_number
import word_pattern
import power_of_three


def test_two_sum():
  assert two_sum.Solution().two_sum([2, 7, 11, 15], 9) == [0, 1]
  assert two_sum.Solution().two_sum([3, 2, 4], 6) == [1, 2]
  assert two_sum.Solution().two_sum([3, 3], 6) == [0, 1]


def test_is_palindrome():
  assert palindrome_number.Solution().is_palindrome(121) == True
  assert palindrome_number.Solution().is_palindrome(-121) == False
  assert palindrome_number.Solution().is_palindrome(10) == False


def test_roman_to_int():
  assert roman_to_integer.Solution().roman_to_int("III") == 3
  assert roman_to_integer.Solution().roman_to_int("LVIII") == 58
  assert roman_to_integer.Solution().roman_to_int("MCMXCIV") == 1994


def test_longest_common_prefix():
  assert longest_common_prefix.Solution().longest_common_prefix(["flower", "flow", "flight"]) == "fl"
  assert longest_common_prefix.Solution().longest_common_prefix(["dog", "racecar", "car"]) == ""
  assert longest_common_prefix.Solution().longest_common_prefix(["cir", "car"]) == "c"


def test_is_valid():
  assert valid_parentheses.Solution().is_valid("()") == True
  assert valid_parentheses.Solution().is_valid("()[]{}") == True
  assert valid_parentheses.Solution().is_valid("(]") == False
  assert valid_parentheses.Solution().is_valid("]") == False
  assert valid_parentheses.Solution().is_valid("){") == False
  assert valid_parentheses.Solution().is_valid("([}}])") == False


def test_str_str():
  assert find_the_index_of_the_first_occurrence_in_a_string.Solution().str_str("sadbutsad", "sad") == 0
  assert find_the_index_of_the_first_occurrence_in_a_string.Solution().str_str("leetcode", "leeto") == -1


def test_search_insert():
  assert search_input_position.Solution().search_insert([1, 3, 5, 6], 5) == 2
  assert search_input_position.Solution().search_insert([1, 3, 5, 6], 2) == 1
  assert search_input_position.Solution().search_insert([1, 3, 5, 6], 7) == 4
  assert search_input_position.Solution().search_insert([1], 1) == 0


def test_length_of_last_word():
  assert length_of_last_word.Solution().length_of_last_word("Hello World") == 5
  assert length_of_last_word.Solution().length_of_last_word("   fly me   to   the moon  ") == 4
  assert length_of_last_word.Solution().length_of_last_word("luffy is still joyboy") == 6
  assert length_of_last_word.Solution().length_of_last_word("a") == 1


def test_plus_one():
  assert plus_one.Solution().plus_one([1, 2, 3]) == [1, 2, 4]
  assert plus_one.Solution().plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
  assert plus_one.Solution().plus_one([9]) == [1, 0]


def test_max_profit():
  assert best_time_to_buy_and_sell_stock.Solution().max_profit([7, 1, 5, 3, 6, 4]) == 5
  assert best_time_to_buy_and_sell_stock.Solution().max_profit([7, 6, 4, 3, 1]) == 0


def test_is_valid_palindrome():
  assert valid_palindrome.Solution().is_valid_palindrome("A man, a plan, a canal: Panama") == True
  assert valid_palindrome.Solution().is_valid_palindrome("race a car") == False
  assert valid_palindrome.Solution().is_valid_palindrome(" ") == True
  assert valid_palindrome.Solution().is_valid_palindrome("ab_a") == True


def test_single_number():
  assert single_number.Solution().single_number([2, 2, 1]) == 1
  assert single_number.Solution().single_number([4, 1, 2, 1, 2]) == 4
  assert single_number.Solution().single_number([1]) == 1


def test_convert_to_title():
  assert excel_sheet_column_title.Solution().convert_to_title(1) == "A"
  assert excel_sheet_column_title.Solution().convert_to_title(28) == "AB"
  assert excel_sheet_column_title.Solution().convert_to_title(701) == "ZY"


def test_majority_element():
  assert majority_element.Solution().majority_element([3, 2, 3]) == 3
  assert majority_element.Solution().majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_title_to_number():
  assert excel_sheet_column_number.Solution().title_to_number("A") == 1
  assert excel_sheet_column_number.Solution().title_to_number("AB") == 28
  assert excel_sheet_column_number.Solution().title_to_number("ZY") == 701


def test_contains_duplicate():
  assert contains_duplicate.Solution().contains_duplicate([1, 2, 3, 1]) == True
  assert contains_duplicate.Solution().contains_duplicate([1, 2, 3, 4]) == False
  assert contains_duplicate.Solution().contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


def test_is_power_of_two():
  assert power_of_two.Solution().is_power_of_two(1) == True
  assert power_of_two.Solution().is_power_of_two(16) == True
  assert power_of_two.Solution().is_power_of_two(3) == False


def test_is_anagram():
  assert valid_anagram.Solution().is_anagram("anagram", "nagaram") == True
  assert valid_anagram.Solution().is_anagram("rat", "car") == False


def test_add_digits():
  assert add_digits.Solution().add_digits(38) == 2
  assert add_digits.Solution().add_digits(0) == 0


def test_missing_number():
  assert missing_number.Solution().missing_number([3, 0, 1]) == 2
  assert missing_number.Solution().missing_number([0, 1]) == 2
  assert missing_number.Solution().missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_word_pattern():
  assert word_pattern.Solution().word_pattern("abba", "dog cat cat dog") == True
  assert word_pattern.Solution().word_pattern("abba", "dog cat cat fish") == False
  assert word_pattern.Solution().word_pattern("aaaa", "dog cat cat dog") == False
  assert word_pattern.Solution().word_pattern("abba", "dog dog dog dog") == False


def test_power_of_three():
  assert power_of_three.Solution().is_power_of_three(27) == True
  assert power_of_three.Solution().is_power_of_three(0) == False
  assert power_of_three.Solution().is_power_of_three(-1) == False
  assert power_of_three.Solution().is_power_of_three(9) == True