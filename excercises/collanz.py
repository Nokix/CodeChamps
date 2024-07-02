from unittest import TestCase
from parameterized import parameterized

""" 1ner-Vermutung ⭐⭐⭐

Die 1ner-Sequenz startet bei einer Zahl n > 1 und folgt den Regeln: 
Wenn n gerade ist, dann n <- n / 2, ansonsten n <- 3n + 1, bis n = 1 erreicht. 

Finde die kleinste Zahl 1 < n < 1.000.000 mit der längsten Sequenz.
Wie lang ist die Sequenz für welches n? 

8 -> 4 -> 2 -> 1 (Länge 4)

5 -> 16 -> 8 -> 4 -> 2 -> 1 (Länge 6)

6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (Länge 9)

Wenn du schaffst zu zeigen, warum die Ketten immer bei 1 enden,
sorge ich persönlich dafür, dass du einen Doktor erhälst.
"""

known_chains = {1: {"l": 1}}


def next_collatz(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def find_and_insert(n):
    next = next_collatz(n)
    if next not in known_chains:
        find_and_insert(next)
    known_chains[n] = {"l": known_chains[next]["l"] + 1, "next": next}


def collatz_sequence(n: int):
    find_and_insert(n)
    result = [n]
    while result[-1] != 1:
        result.append(known_chains[result[-1]]["next"])
    return result


def find_longest_collanz_sequenz(limit_inclusive):
    candidates = range(2, limit_inclusive + 1)

    for n in candidates:
        find_and_insert(n)

    all_lengths = [chain_info["l"] for chain_start, chain_info in known_chains.items() if
                   chain_start <= limit_inclusive]
    longest_len = max(all_lengths)

    longest_chain_starts = [chain_start for chain_start, chain_info in known_chains.items()
                            if chain_info["l"] == longest_len and chain_start <= limit_inclusive]

    print(collatz_sequence(min(longest_chain_starts)))

    return longest_len, min(longest_chain_starts)


class CollatzSequenceTest(TestCase):
    @parameterized.expand([
        ([2, 1], 2),
        ([8, 4, 2, 1], 8),
        ([5, 16, 8, 4, 2, 1], 5),
        ([6, 3, 10, 5, 16, 8, 4, 2, 1], 6),
    ])
    def test_collatz_sequence(self, expected, start_number):
        self.assertListEqual(expected, list(collatz_sequence(start_number)))

    @parameterized.expand([
        (2, 2, 2),
        (8, 3, 3),
        (8, 3, 4),
        (8, 3, 5),
        (179, 871, 1000),
        (525, 837799, 1000000)  # Lösung
    ])
    def test_longest_collanz_sequence(self, expected_len, expected_i, limit):
        self.assertTupleEqual((expected_len, expected_i), find_longest_collanz_sequenz(limit))


if __name__ == '__main__':
    number = 871
    print(collatz_sequence(number))
    print(len(collatz_sequence(number)))
