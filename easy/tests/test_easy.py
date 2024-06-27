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
import move_zeroes
import word_pattern
import power_of_three
import power_of_four
import reverse_string
import reverse_vowels_of_a_string


def test_two_sum():

  solution = two_sum.Solution()

  assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
  assert solution.two_sum([3, 2, 4], 6) == [1, 2]
  assert solution.two_sum([3, 3], 6) == [0, 1]


def test_is_palindrome():

  solution = palindrome_number.Solution()

  assert solution.is_palindrome(121) == True
  assert solution.is_palindrome(-121) == False
  assert solution.is_palindrome(10) == False


def test_roman_to_int():

  solution = roman_to_integer.Solution()

  assert solution.roman_to_int("III") == 3
  assert solution.roman_to_int("LVIII") == 58
  assert solution.roman_to_int("MCMXCIV") == 1994


def test_longest_common_prefix():

  solution = longest_common_prefix.Solution()

  assert solution.longest_common_prefix(["flower", "flow", "flight"]) == "fl"
  assert solution.longest_common_prefix(["dog", "racecar", "car"]) == ""
  assert solution.longest_common_prefix(["cir", "car"]) == "c"


def test_is_valid():

  solution = valid_parentheses.Solution()

  assert solution.is_valid("()") == True
  assert solution.is_valid("()[]{}") == True
  assert solution.is_valid("(]") == False
  assert solution.is_valid("]") == False
  assert solution.is_valid("){") == False
  assert solution.is_valid("([}}])") == False


def test_str_str():

  solution = find_the_index_of_the_first_occurrence_in_a_string.Solution()

  assert solution.str_str("sadbutsad", "sad") == 0
  assert solution.str_str("leetcode", "leeto") == -1


def test_search_insert():

  solution = search_input_position.Solution()

  assert solution.search_insert([1, 3, 5, 6], 5) == 2
  assert solution.search_insert([1, 3, 5, 6], 2) == 1
  assert solution.search_insert([1, 3, 5, 6], 7) == 4
  assert solution.search_insert([1], 1) == 0


def test_length_of_last_word():

  solution = length_of_last_word.Solution()

  assert solution.length_of_last_word("Hello World") == 5
  assert solution.length_of_last_word("   fly me   to   the moon  ") == 4
  assert solution.length_of_last_word("luffy is still joyboy") == 6
  assert solution.length_of_last_word("a") == 1


def test_plus_one():

  solution = plus_one.Solution()

  assert solution.plus_one([1, 2, 3]) == [1, 2, 4]
  assert solution.plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
  assert solution.plus_one([9]) == [1, 0]


def test_max_profit():

  solution = best_time_to_buy_and_sell_stock.Solution()

  assert solution.max_profit([7, 1, 5, 3, 6, 4]) == 5
  assert solution.max_profit([7, 6, 4, 3, 1]) == 0


def test_is_valid_palindrome():

  solution = valid_palindrome.Solution()

  assert solution.is_valid_palindrome("A man, a plan, a canal: Panama") == True
  assert solution.is_valid_palindrome("race a car") == False
  assert solution.is_valid_palindrome(" ") == True
  assert solution.is_valid_palindrome("ab_a") == True


def test_single_number():

  solution = single_number.Solution()

  assert solution.single_number([2, 2, 1]) == 1
  assert solution.single_number([4, 1, 2, 1, 2]) == 4
  assert solution.single_number([1]) == 1


def test_convert_to_title():

  solution = excel_sheet_column_title.Solution()

  assert solution.convert_to_title(1) == "A"
  assert solution.convert_to_title(28) == "AB"
  assert solution.convert_to_title(701) == "ZY"


def test_majority_element():

  solution = majority_element.Solution()

  assert solution.majority_element([3, 2, 3]) == 3
  assert solution.majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_title_to_number():

  solution = excel_sheet_column_number.Solution()

  assert solution.title_to_number("A") == 1
  assert solution.title_to_number("AB") == 28
  assert solution.title_to_number("ZY") == 701


def test_contains_duplicate():

  solution = contains_duplicate.Solution()

  assert solution.contains_duplicate([1, 2, 3, 1]) == True
  assert solution.contains_duplicate([1, 2, 3, 4]) == False
  assert solution.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


def test_is_power_of_two():

  solution = power_of_two.Solution()

  assert solution.is_power_of_two(1) == True
  assert solution.is_power_of_two(16) == True
  assert solution.is_power_of_two(3) == False


def test_is_anagram():

  solution = valid_anagram.Solution()

  assert solution.is_anagram("anagram", "nagaram") == True
  assert solution.is_anagram("rat", "car") == False


def test_add_digits():

  solution = add_digits.Solution()

  assert solution.add_digits(38) == 2
  assert solution.add_digits(0) == 0


def test_missing_number():

  solution = missing_number.Solution()

  assert solution.missing_number([3, 0, 1]) == 2
  assert solution.missing_number([0, 1]) == 2
  assert solution.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_move_zeroes():

  solution = move_zeroes.Solution()

  nums_1 = [0, 1, 0, 3, 12]
  solution.move_zeroes(nums_1)
  assert nums_1 == [1, 3, 12, 0, 0]

  nums_2 = [0]
  solution.move_zeroes(nums_2)
  assert nums_2 == [0]


def test_word_pattern():

  solution = word_pattern.Solution()

  assert solution.word_pattern("abba", "dog cat cat dog") == True
  assert solution.word_pattern("abba", "dog cat cat fish") == False
  assert solution.word_pattern("aaaa", "dog cat cat dog") == False
  assert solution.word_pattern("abba", "dog dog dog dog") == False


def test_is_power_of_three():

  solution = power_of_three.Solution()

  assert solution.is_power_of_three(27) == True
  assert solution.is_power_of_three(0) == False
  assert solution.is_power_of_three(-1) == False
  assert solution.is_power_of_three(9) == True


def test_is_power_of_four():

  solution = power_of_four.Solution()

  assert solution.is_power_of_four(16) == True
  assert solution.is_power_of_four(5) == False
  assert solution.is_power_of_four(1) == True


def test_reverse_string():

  solution = reverse_string.Solution()

  s_1 = ["h", "e", "l", "l", "o"]
  solution.reverse_string(s_1)
  assert s_1 == ["o", "l", "l", "e", "h"]

  s_2 = ["H", "a", "n", "n", "a", "h"]
  solution.reverse_string(s_2)
  assert s_2 == ["h", "a", "n", "n", "a", "H"]


def test_reverse_vowels():

  solution = reverse_vowels_of_a_string.Solution()

  assert solution.reverse_vowels("hello") == "holle"
  assert solution.reverse_vowels("leetcode") == "leotcede"
  assert solution.reverse_vowels("a.") == "a."
