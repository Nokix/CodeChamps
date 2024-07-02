"""Deadfish Decoder⭐⭐
Bei der sogenannten "esoterischen Programmiersprache" Deadfish gibt es genau vier Anweisungen:
d (decrease), i (increase), s (square) und o (output).
Gearbeitet wird mit exakt einem Byte. Dieses beginnt beim Wert 0.
Durch Kombinationen der vier Anweisungen steuern wir die ASCII-Werte der gewünschen Zeichen an.

Möchten wir beispielsweise ein Ausrufezeichen (!) setzen (ASCII-Wert 33),
dann könnten wir wie folgt vorgehen:

iiiiiisdddo

Wir erhöhen sechs Mal (sind dann beim Wert 6), quadrieren dann (mit s, sind also bei 36)
und ziehen drei ab (drei mal d).
Wenn wir nun den Output machen, dann wird auf der Konsole das Ausrufezeichen ausgegeben.

Bei 255 findet der Überlauf statt, die 256 wird also durch 0 ersetzt.
Wenn wir bei 0 sind und dekrementieren, landen wir bei 255.
Schreibe ein Programm, das folgenden Deadfish-Code interpretiert:

dddsisdsddoddssiiiiodoiisioiisdddoisdodddsiiiioisissddoiiiodddddsddoddoiisdddoiso
"""


def num_to_char(num):
    return chr(num)


def decode(code):
    cell = 0
    output = ""

    for c in code:
        if c == "i":
            cell = (cell + 1) % 256
        elif c == "d":
            cell = (cell - 1) % 256
        elif c == "s":
            cell = (cell ** 2) % 256
        elif c == "o":
            output += num_to_char(cell)

    return output


"""Deadfish Encoder⭐⭐⭐

Bei der sogenannten "esoterischen Programmiersprache" Deadfish gibt es genau vier Anweisungen:
d (decrease), i (increase), s (square) und o (output).
Gearbeitet wird mit exakt einem Byte. Dieses beginnt beim Wert 0.
Durch Kombinationen der vier Anweisungen steuern wir die ASCII-Werte der gewünschen Zeichen an.
 
Möchten wir beispielsweise ein Ausrufezeichen (!) setzen (ASCII-Wert 33), dann könnten wir wie folgt vorgehen:
iiiiiisdddo
Wir erhöhen sechs Mal (sind dann beim Wert 6), quadrieren dann (mit s, sind also bei 36) und ziehen drei ab (drei mal d). Wenn wir nun den Output machen, dann wird auf der Konsole das Ausrufezeichen ausgegeben.
Bei 255 findet der Überlauf statt, die 256 wird also durch 0 ersetzt. Wenn wir bei 0 sind und dekrementieren, landen wir bei 255.
 
Schreibe ein Programm, der aus einem Klartext den kürzestmöglichen Deadfishcode generiert."""
def encode(text):
    return "o".join(bfs(ord(start), ord(target)) for start, target in zip('\x00' + text, text)) + "o"


def get_options(a):
    yield (a + 1) % 256, "i"
    yield (a - 1) % 256, "d"
    yield (a ** 2) % 256, "s"


def bfs(start, target):
    queue = [(start % 256, target % 256, "")]
    while queue:
        current_start, target, output = queue.pop(0)
        if current_start == target:
            return output
        for new_start, appendix in get_options(current_start):
            queue.append((new_start, target, output + appendix))


if __name__ == '__main__':
    to_decode = "dddsisdsddoddssiiiiodoiisioiisdddoisdodddsiiiioisissddoiiiodddddsddoddoiisdddoiso"
    print(decode(to_decode))

    encoded = encode("Guten Morgen!")
    print(encoded)
    print(decode(encoded))
