import math


def evaluate_special_operations(eingabe, taste):
    laenge = 0
    berechnendeZahl = ""
    test = 0
    result = ""

    for zeichen in eingabe:
        if test == 1 and zeichen != "]":
            berechnendeZahl += zeichen

        if test == 1 and zeichen == "]":
            if taste == "log":
                result = str(math.log10(int(berechnendeZahl)))
            elif taste == "cos":
                result = str(math.cos(int(berechnendeZahl)))
            elif taste == "sin":
                result = str(math.sin(int(berechnendeZahl)))
            elif taste == "tan":
                result = str(math.tan(int(berechnendeZahl)))
            elif taste == "sqrt":
                result = str(math.sqrt(int(berechnendeZahl)))

        if zeichen == "[":
            test = 1
        else:
            laenge += 1

    return result, laenge


def trapezSumme(formel, a, b, n):
    h = (b - a) / n

    # Berechne ersten und letzten Wert der Funktion
    y_first = calculate(formel, a)
    y_last = calculate(formel, b)

    # Berechne mittlere Werte der Funktion
    intermediate_sum = sum(calculate(formel, a + i * h) for i in range(1, n))

    # Berechne die Trapezsumme
    trapezoidal_sum = h * ((y_first + y_last) / 2 + intermediate_sum)

    # Runde das Ergebnis und gebe es im Ergebnis-Entry aus
    trapezoidal_sum = round(trapezoidal_sum, 7)
    return trapezoidal_sum


def calculate(formel, value):
    x = value
    return eval(formel)
