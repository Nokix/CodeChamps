from unittest import TestCase
from parameterized import parameterized

""" Palindromzahlen ⭐
Wie viele Palindromzahlen gibt es zwischen 10000 und 100000?

Eine Palindromzahl ist von Vorne und von Hinten gleich zu lesen,

z.B. ist 12321 eine Palindromzahl und 12311 ist keine.
"""


def is_palindronnumber(n: int):
    n_str = str(n)
    return n_str == n_str[::-1]


def count_palindroms(min_inclusive, max_exclusive):
    return sum(is_palindronnumber(n) for n in range(min_inclusive, max_exclusive))


class PalindromNumbersTest(TestCase):
    @parameterized.expand([
        (True, 1),
        (True, 11),
        (True, 121),
        (True, 10201),
        (True, 11111),
        (True, 1221),
        (False, 11131),
        (False, 1313),

    ])
    def test_ispalindronnumber(self, expected, number):
        self.assertEqual(expected, is_palindronnumber(number))

    @parameterized.expand([
        (1, 10, 20),
        (0, 15, 20),
        (10, 100, 200),
        (100, 100, 2000),
        (900, 10000, 100000),
    ])
    def test_count_palindroms(self, expected, min_inclusive, max_exclusive):
        self.assertEqual(expected, count_palindroms(min_inclusive, max_exclusive))
