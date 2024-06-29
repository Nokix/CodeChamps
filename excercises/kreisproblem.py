from unittest import TestCase
from parameterized import parameterized

""" Kreisproblem ⭐
10000 Leute stehen im Kreis. Sie sind durchnummeriert von 0 bis 9999.

Jeder 3. wird entfernt. Das geschieht so lange, bis nur noch 2 übrig bleiben.

Welche beiden bleiben übrig?

Beispiel: Wenn 6 Leute im Kreis stehen würden, wären am Ende noch die 0 und 4 übrig.
"""


def kreisproblem(n: int):
    elements = list(range(n))
    while len(elements) > 2:
        elements = elements[3:] + elements[:2]
    return elements[0], elements[1]


class KreisproblemTest(TestCase):
    @parameterized.expand([
        (0, 1, 2),
        (0, 1, 3),
        (0, 3, 4),
        (1, 3, 5),
        (0, 4, 6),
        (8922, 2691, 10000)  # Antwort
    ])
    def test_kreisproblem(self, expected_a, expected_b, n):
        self.assertCountEqual((expected_a, expected_b), kreisproblem(n))
