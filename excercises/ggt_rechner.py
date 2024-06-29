from unittest import TestCase
from parameterized import parameterized

"""GGT-Rechner ⭐
Erstelle ein Programm, dass von beliebig vielen Zahlen den GGT (größten gemeinsamen Teiler)
ausrechnen. Von welchen Zahlen genau du den GGT ausrechnen sollst, sagt dir der Trainer.

Beispiele:
ggt(28, 12) = 4
ggt(128, 40, 150) = 2
ggt(22, 11) = 11
ggt(33, 22, 7) = 1
ggt(12) = 12
ggt(12, 12) = 12
ggt(6, 12, 18, 21) = 3
"""


def ggt(*nums):
    return max((teiler for teiler in range(1, max(nums) + 1) if not any(num % teiler for num in nums)), default=1)


class GGTTest(TestCase):
    @parameterized.expand([
        ((28, 12), 4),
        ((128, 40, 150), 2),
        ((22, 11), 11),
        ((33, 22, 7), 1),
        ((12,), 12),
        ((12, 12), 12),
        ((6, 12, 18, 21), 3),
    ])
    def test_ispalindronnumber(self, nums, expected_ggt):
        self.assertEqual(expected_ggt, ggt(*nums))
