"""Raketenstart ⭐
Du hast eine Rakete gebaut. Diese wiegt 700 t, wenn sie noch nicht betankt ist.
Um 1 t Gewicht in den Kosmos zu befördern, brauchst du exakt 58,912 kg Treibstoff.
Wie viel wird deine Rakete wiegen, wenn du sie erfolgreich in den Kosmos schießen willst?

Berechne auf 10 Nachkommastellen genau.
"""


EMPTY_WEIGHT = 700
GAS_PER_WEIGHT = 0.058912
def needed_gas(weight):
    return weight * GAS_PER_WEIGHT

def repeated_calc(initial=EMPTY_WEIGHT, func=needed_gas, times=3):
    result = initial
    diff = initial
    for _ in range(times):
        diff = func(diff)
        result += diff
    return result

if __name__ == '__main__':
    for i in range(0, 20):
        print(f"{i}: {repeated_calc(times=i)}")
        # 743.8199190723