"""

https://projecteuler.net/problem=419


The look and say sequence goes 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
The sequence starts with 1 and all other members are obtained by describing
the previous member in terms of consecutive digits.

It helps to do this out loud:
1 is 'one one' → 11
11 is 'two ones' → 21
21 is 'one two and one one' → 1211
1211 is 'one one, one two and two ones' → 111221
111221 is 'three ones, two twos and one one' → 312211

Was die 73-ste Zahl.

"""

def describe(n):
    return int(describe_intern(n))

def describe_intern(n):
    if not n:
        return ""
    s = str(n)
    count_first = count_repeat_first(s)
    return str(count_first) + s[0] + describe_intern(s[count_first:])


def count_repeat_first(s):
    if not s:
        return 0
    first_letter = s[0]
    count = 1
    for c in s[1:]:
        if c == first_letter:
            count += 1
        else:
            break
    return count


from unittest import TestCase
from parameterized import parameterized


class DescribeTest(TestCase):
    @parameterized.expand([
        (1, 11),
        (11, 21),
        (21, 1211),
        (1211, 111221),
        (111221, 312211),
    ])
    def test_describe(self, number, described_number):
        self.assertEqual(described_number, describe(number))

    def test_describe(self):
        n = 1
        for i in range(73):
            print(f"{i}: 1-sen: {str(n).count("3")} {n}")
            n = describe(n)

if __name__ == '__main__':
    print(describe(25).count("1"))
