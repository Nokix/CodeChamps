from unittest import TestCase
from parameterized import parameterized

""" Goldbach ⭐
Wusstest du, dass 3779 und 3593 beides Primzahlen sind?
Und wusstest du, dass 3593 + 3779 + 1 = 7373 ergibt?

Welche anderen Primzahlpärchen (a,b) mit a <= b gibt es insgesamt,
die a + b + 1 = 7373 ergeben?
"""


def is_prime(n: int):
    if n <= 1:
        return False

    for teiler in range(2, n // 2 + 1):
        if not n % teiler:
            return False
    return True


def find_goldbach_primes(n):
    all_primes = [p for p in range(2, n) if is_prime(p)]
    return [(a, b) for a in all_primes for b in all_primes if a <= b and a + b == n]


class GoldbachTest(TestCase):
    @parameterized.expand([
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (12, False),
        (13, True)

    ])
    def test_isprime(self, number, is_prime_number):
        self.assertEqual(is_prime(number), is_prime_number)

    @parameterized.expand([
        (4, [(2, 2)]),
        (6, [(3, 3)]),
        (8, [(3, 5)]),
        (10, [(5, 5), (3, 7)]),
        (12, [(5, 7)]),
        (24, [(11, 13), (5, 19), (7, 17)]),
        (7372, [(3, 7369), (23, 7349), (41, 7331), (89, 7283), (179, 7193),
                (251, 7121), (263, 7109), (269, 7103), (293, 7079), (353, 7019),
                (359, 7013), (389, 6983), (401, 6971), (461, 6911), (503, 6869),
                (509, 6863), (569, 6803), (593, 6779), (653, 6719), (683, 6689),
                (719, 6653), (773, 6599), (809, 6563), (821, 6551), (881, 6491),
                (983, 6389), (1013, 6359), (1019, 6353), (1049, 6323), (1061, 6311),
                (1103, 6269), (1109, 6263), (1151, 6221), (1229, 6143), (1259, 6113),
                (1283, 6089), (1319, 6053), (1361, 6011), (1433, 5939), (1493, 5879),
                (1511, 5861), (1523, 5849), (1559, 5813), (1571, 5801), (1721, 5651),
                (1733, 5639), (1871, 5501), (1889, 5483), (1901, 5471), (1931, 5441),
                (1973, 5399), (1979, 5393), (2039, 5333), (2063, 5309), (2069, 5303),
                (2099, 5273), (2111, 5261), (2141, 5231), (2273, 5099), (2333, 5039),
                (2351, 5021), (2399, 4973), (2441, 4931), (2579, 4793), (2621, 4751),
                (2693, 4679), (2699, 4673), (2729, 4643), (2789, 4583), (2879, 4493),
                (2909, 4463), (2963, 4409), (2999, 4373), (3023, 4349), (3083, 4289),
                (3089, 4283), (3119, 4253), (3299, 4073), (3323, 4049), (3359, 4013),
                (3371, 4001), (3449, 3923), (3461, 3911), (3491, 3881), (3539, 3833),
                (3593, 3779), (3671, 3701)])  # 87 Elemente
    ])
    def test_find_goldbach_primes(self, number, primes):
        self.assertCountEqual(primes, find_goldbach_primes(number))


if __name__ == '__main__':
    print(find_goldbach_primes(7372))
