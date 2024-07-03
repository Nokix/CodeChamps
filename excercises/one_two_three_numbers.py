# https://projecteuler.net/problem=698

def nth_123number(n):
    if n in nth_123number.store:
        return nth_123number.store[n]

    next_candidate = nth_123number(n - 1) + 1
    while not is_123number(next_candidate):
        next_candidate += 1

    nth_123number.store[n] = next_candidate
    return next_candidate


nth_123number.store = {0: 0, 1: 1}


def is_123number(n):
    n_str = str(n)
    counts = [n_str.count(str(i)) for i in (1, 2, 3)]
    return len(n_str) == sum(counts) and all(count in nth_123number.store.values() for count in counts)


if __name__ == '__main__':
    nth_123number(73)
    print(nth_123number.store)
