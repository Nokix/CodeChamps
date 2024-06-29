from unittest import TestCase, main
from parameterized import parameterized

# TODO: Aufgabenstellung erstellen

rome_to_dec_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

dec_to_rome_dict = {d: r for r, d in rome_to_dec_dict.items()}


def rome_to_dec(rome):
    i = 0
    num = 0
    while i < len(rome):
        if i + 1 < len(rome) and rome[i:i + 2] in rome_to_dec_dict:
            num += rome_to_dec_dict[rome[i:i + 2]]
            i += 2
        else:
            num += rome_to_dec_dict[rome[i]]
            i += 1
    return num


def dec_to_rome(dec):
    result = []
    for value, symbol in sorted(dec_to_rome_dict.items(), key=lambda i: i[0], reverse=True):
        while dec >= value:
            result.append(symbol)
            dec -= value
    return ''.join(result)


class RomeNumbersTest(TestCase):
    test_data = [
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("IV", 4),
        ("V", 5),
        ("VI", 6),
        ("VII", 7),
        ("VIII", 8),
        ("IX", 9),
        ("X", 10),
        ("XI", 11),
        ("XII", 12),
        ("XIII", 13),
        ("XIV", 14),
        ("XV", 15),
        ("XVI", 16),
        ("XVII", 17),
        ("XVIII", 18),
        ("XIX", 19),
        ("XX", 20),
        ("XXI", 21),
        ("XLIV", 44),
        ("LXXIII", 73),
        ("LXXXVIII", 88),
        ("XCIX", 99),
        ("C", 100),
    ]

    @parameterized.expand(test_data)
    def test_rome_to_dec(self, rome, dec):
        self.assertEqual(dec, rome_to_dec(rome))

    @parameterized.expand(test_data)
    def test_dec_to_rome(self, rome, dec):
        self.assertEqual(rome, dec_to_rome(dec))


if __name__ == '__main__':
    main()
