import tkinter as tk
import math


class Taschenrechner:
    ##INITIALISIERUNG FENSTER##
    def __init__(self, master):
        self.master = master
        root.title("Taschenrechner")
        root.geometry("700x650")

        # Variablen zur Platzierung der Entries
        formel_entry_x = 100
        eingabe_entry_y = 50

        ergebnis_entry_x = 350

        # Definierung und Platzierung des Eingabe Entry
        self.formelEntry = tk.Entry(root, width=30, justify="center")
        self.formelEntry.place(x=formel_entry_x, y=eingabe_entry_y)
        # Definierung und Platzierung des Ergebnis Entry
        self.ergebnisEntry = tk.Entry(root, width=30, justify="center")
        self.ergebnisEntry.place(x=ergebnis_entry_x, y=eingabe_entry_y)

        trapez_x = 100
        trapez_y = 575
        self.aEntry = tk.Entry(root, justify="center")
        self.aEntry.place(x=trapez_x, y=trapez_y, width=100)
        self.bEntry = tk.Entry(root, justify="center")
        self.bEntry.place(x=(trapez_x + 125), y=trapez_y, width=100)
        self.nEntry = tk.Entry(root, justify="center")
        self.nEntry.place(x=(trapez_x + 250), y=trapez_y, width=100)

        Labels = [tk.Label(root, text="Startpunkt"), tk.Label(root, text="Endpunkt"),
                  tk.Label(root, text="Anzahl Trapeze")]
        zaehlLabel = 0
        abstandLabel = 25
        for label in Labels:
            if zaehlLabel == 0:
                label.place(x=trapez_x, y=(trapez_y - abstandLabel))
            elif zaehlLabel == 1:
                label.place(x=(trapez_x + 125), y=(trapez_y - abstandLabel))
            elif zaehlLabel == 2:
                label.place(x=(trapez_x + 250), y=(trapez_y - abstandLabel))
            zaehlLabel += 1

        # Definierung und Platzierung des Labels für Gleichzeichen
        gleich = tk.Label(root, text="=")
        gleich.place(x=formel_entry_x + 210, y=eingabe_entry_y - 3)

        # Sammlung der Knöpfe
        Button = [tk.Button(root, text="AC", command=self.deleteAll, width=10, height=4),
                  tk.Button(root, text="/", command=lambda: self.taste_gedrueckt("/"), width=10, height=4),
                  tk.Button(root, text="*", command=lambda: self.taste_gedrueckt("*"), width=10, height=4),
                  tk.Button(root, text="DEL", command=self.deleteLast, width=10, height=4),

                  tk.Button(root, text="7", command=lambda: self.taste_gedrueckt("7"), width=10, height=4),
                  tk.Button(root, text="8", command=lambda: self.taste_gedrueckt("8"), width=10, height=4),
                  tk.Button(root, text="9", command=lambda: self.taste_gedrueckt("9"), width=10, height=4),
                  tk.Button(root, text="-", command=lambda: self.taste_gedrueckt("-"), width=10, height=4),

                  tk.Button(root, text="4", command=lambda: self.taste_gedrueckt("4"), width=10, height=4),
                  tk.Button(root, text="5", command=lambda: self.taste_gedrueckt("5"), width=10, height=4),
                  tk.Button(root, text="6", command=lambda: self.taste_gedrueckt("6"), width=10, height=4),
                  tk.Button(root, text="+", command=lambda: self.taste_gedrueckt("+"), width=10, height=4),

                  tk.Button(root, text="1", command=lambda: self.taste_gedrueckt("1"), width=10, height=4),
                  tk.Button(root, text="2", command=lambda: self.taste_gedrueckt("2"), width=10, height=4),
                  tk.Button(root, text="3", command=lambda: self.taste_gedrueckt("3"), width=10, height=4),

                  tk.Button(root, text="=", command=self.berechne, width=10, height=4),

                  tk.Button(root, text="%", command=lambda: self.taste_gedrueckt("%"), width=10, height=4),
                  tk.Button(root, text="0", command=lambda: self.taste_gedrueckt("0"), width=10, height=4),
                  tk.Button(root, text=".", command=lambda: self.taste_gedrueckt("."), width=10, height=4),
                  tk.Button(root, text="^", command=lambda: self.taste_gedrueckt("**"), width=10, height=4),

                  tk.Button(root, text="x", command=lambda: self.taste_gedrueckt("x"), width=5, height=2),
                  tk.Button(root, text="sqrt", command=self.wurzelFormel, width=5, height=2),
                  tk.Button(root, text="log", command=self.logFormel, width=5, height=2),
                  tk.Button(root, text="(", command=lambda: self.taste_gedrueckt("("), width=5, height=2),
                  tk.Button(root, text=")", command=lambda: self.taste_gedrueckt(")"), width=5, height=2)

                  ]

        # Variablen zur Positionierung der Knöpfe. Variablen geben den Ausgangspunkt des ersten Knopfes aus,
        # Wert wird in Funktion später verändert
        buttonzaehl = 0
        xButton = 100
        yButton = 100
        reihen = 0
        abstandX = 85
        # Platzieren der Buttons mit for-schleife. Buttons werden mit jedem Durchlauf um gegebenen Wert nach rechts
        # verschoben. Nach 4 Knöpfen wird eine neue Reihe angefangen und der x-Wert auf den Startwert zurückgesetzt.
        # Hierdurch wird ein Grid an Knöpfen erstellt
        for button in Button:
            button.place(x=xButton, y=yButton)
            xButton += abstandX
            buttonzaehl += 1
            # 4 gibt die Anzahl der Spalten an Knöpfen an. 4 = 4 Spalten
            if buttonzaehl == 4:
                xButton -= 340
                yButton += 75
                buttonzaehl = 0
                reihen += 1
            if reihen == 5:
                buttonzaehl = -1
                abstandX /= 1.5
                reihen = 0

        Button2 = [tk.Button(root, text="TrapezSumme-Start", command=self.trapezSummeStart, width=20),
                   tk.Button(root, text="TrapezSumme-Ende", command=self.trapezSummeEnde, width=20),
                   tk.Button(root, text="TrapezSumme-Zahl", command=self.trapezSummeZahl, width=20),
                   tk.Button(root, text="Rechner", command=self.rechnerEntry, width=20),
                   tk.Button(root, text="Trapez-Rechnung", command=self.trapezSumme, width=20)]

        trapezButtonX = 450
        trapezButtonY = 200

        for button in Button2:
            button.place(x=trapezButtonX, y=trapezButtonY)
            trapezButtonY += 50

        root.mainloop()

    def test(self):
        pass

    ##FUNKTIONEN##
    wurzelStart = 0

    def wurzelFormel(self):
        if self.wurzelStart == 1:
            self.wurzelStart = 0
            self.formelEntry.insert("end", "]")
            wurzel = self.formelEntry.get()
            laenge = 0
            bruch = ""
            test = 0
            for zeichen in wurzel:
                if test == 1 and zeichen != "]":
                    bruch += zeichen
                    self.formelEntry.delete(laenge - 4, "end")
                if test == 1 and zeichen == "]":
                    self.wurzelRechnung(bruch)
                if zeichen == "[":
                    self.formelEntry.delete(laenge - 4, laenge + 1)
                    test = 1
                else:
                    laenge += 1
        else:
            self.wurzelStart = 1
            self.formelEntry.insert("end", "sqrt[")

    def wurzelRechnung(self, bruch):
        self.formelEntry.insert("end", str(math.sqrt((int(bruch)))))

    logStart = 0

    def logFormel(self):
        if self.logStart == 1:
            self.logStart = 0
            self.formelEntry.insert("end", "]")
            logarithmus = self.formelEntry.get()
            laenge = 0
            log = ""
            test = 0
            for zeichen in logarithmus:
                if test == 1 and zeichen != "]":
                    log += zeichen
                    self.formelEntry.delete(laenge - 3, "end")
                if test == 1 and zeichen == "]":
                    self.logRechnung(log)
                if zeichen == "[":
                    self.formelEntry.delete(laenge - 3, laenge + 1)
                    test = 1
                else:
                    laenge += 1
        else:
            self.logStart = 1
            self.formelEntry.insert("end", "log[")

    def logRechnung(self, log):
        self.formelEntry.insert("end", str(math.log10((int(log)))))

    # Funktion fügt Formel-Entry gegebenes Symbol an. Symbol entspricht dem auf dem Knopf angezeigten
    def taste_gedrueckt(self, taste):
        if self.eingabeEntry == 0:
            self.formelEntry.insert("end", taste)
        elif self.eingabeEntry == 1:
            self.aEntry.insert("end", taste)
        elif self.eingabeEntry == 2:
            self.bEntry.insert("end", taste)
        elif self.eingabeEntry == 3:
            self.nEntry.insert("end", taste)

    # Funktion berechnet die gegebene Funktion mit der eval Methode von Python. vorher wird überprüft,
    # ob die gegebene Formel eine berechenbare Formel ist oder nicht. Ist diese nicht berechenbar,
    # wird das Eingabefeld rot gefärbt und eine Nachricht im Ergebnis-Entry ausgegeben. Andernfalls färbt sich die
    # Eingabe weiß und die Rechnung wird durchgeführt, anschließend im Ergebnis-Entry eingefügt
    def berechne(self):
        # noinspection PyBroadException
        try:
            self.formelEntry.config(background="white")
            ergebnis = eval(self.formelEntry.get())
            self.ergebnisEntry.delete(0, "end")
            self.ergebnisEntry.insert(0, ergebnis)
        except:
            self.formelEntry.config(background="red")
            self.ergebnisEntry.delete(0, "end")
            self.ergebnisEntry.insert(0, "Fehler bei Eingabe. Kontrolliere")

    # Funktion ermittelt Länge der gegebenen Formel und löscht dann das letzte Element der Formel
    def deleteLast(self):
        wort = self.formelEntry.get()
        laenge = len(wort)
        self.formelEntry.delete((laenge - 1), "end")

    # Funktion löscht sowohl die gesamte Eingabe als auch das Ergebnis
    def deleteAll(self):
        self.formelEntry.config(background="white")
        self.formelEntry.delete(0, "end")
        self.ergebnisEntry.delete(0, "end")

        self.aEntry.delete(0, "end")
        self.bEntry.delete(0, "end")
        self.nEntry.delete(0, "end")

    eingabeEntry = 0

    def trapezSummeStart(self):
        self.eingabeEntry = 1

    def trapezSummeEnde(self):
        self.eingabeEntry = 2

    def trapezSummeZahl(self):
        self.eingabeEntry = 3

    def rechnerEntry(self):
        self.eingabeEntry = 0

    def calculate(self, value):
        # noinspection PyUnusedLocal
        x = value
        return eval(self.formelEntry.get())

    def trapezSumme(self):
        summe2 = 0

        a = int(self.aEntry.get())
        b = int(self.bEntry.get())
        n = int(self.nEntry.get())

        Ts = []
        h = (b - a) / n
        for i in range(n + 1):
            xi = a + (i * h)
            yi = self.calculate(xi)
            Ts.append(yi)
        summe1 = ((Ts[0] + Ts[n]) / 2)
        for i in range(1, n):
            summe2 += Ts[i]
        summe1 = (summe1 + summe2) * h
        summe1 = round(summe1, 7)
        self.ergebnisEntry.delete(0, "end")
        self.ergebnisEntry.insert(0, summe1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Taschenrechner(master=root)
    root.mainloop()
