from unittest import TestCase
from parameterized import parameterized


def prepare_text(text):
    return "".join(c for c in text.lower() if c.isalpha())


def is_palindrom(text):
    return text == text[::-1]


def get_palindroms(text, min_length=2):
    return [text[a:b] for a in range(len(text)) for b in range(a + min_length, len(text)+1) if is_palindrom(text[a:b])]


class PalindromTest(TestCase):
    @parameterized.expand([
        ("Ein Eis esse sie nie, sagt Otto", 2, ['eineisessesienie', 'ineisessesieni', 'neisessesien', 'eisessesie',
                                                'isessesi', 'ses', 'sesses', 'esse', 'ss', 'ses', 'tot', 'otto', 'tt']),
        ("", 2, []),
        ("Aloah", 2, []),
        ("Otto", 2, ["otto", "tt"])

    ])
    def test_get_palindroms(self, text, min_length, expected_palindroms):
        palindroms = get_palindroms(prepare_text(text), min_length=min_length)
        print(palindroms)
        self.assertCountEqual(palindroms, expected_palindroms)


if __name__ == '__main__':
    text = "Ein Eis esse sie nie, sagt Otto"
    print(get_palindroms(prepare_text(text)))
