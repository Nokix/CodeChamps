"""Fibonnaccis Bruder⭐
Die Fibbonacci-Folge beginnt mit den Zahlen 0 und 1.
Wenn Die Beiden Startzahlen -3 und -4 sind, was ist dann der 1000-ste Eintrag?

"""

def fib(n, s0, s1):
    if n == 0:
        return s0
    return fib(n - 1, s1, s0 + s1)


if __name__ == '__main__':
    start0 = -3
    start1 = -4
    for i in [72]:
        print(fib(i, start0, start1), end=" ")

