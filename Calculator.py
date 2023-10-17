import tkinter as tk
from Calculator_Function import *


class Taschenrechner:
    ##Variablen##
    # Variablen zur Platzierung der Entries
    formel_entry_x = 100
    eingabe_entry_y = 50
    ergebnis_entry_x = 335
    trapez_x = 100
    trapez_y = 575
    # Variablen zur Platzierung der Labels
    zaehl_label = 0
    abstand_label = 25
    # Variable für if Fälle bei Wurzelrechnung, bestimmt welcher Fall gewählt wird
    sqrt_log_cos_sin_tanStart = 0
    # Variablen zur Positionierung der Knöpfe. Variablen geben den Ausgangspunkt des ersten Knopfes aus,
    # Wert wird in Funktion später verändert
    x_button = 100
    y_button = 100
    button_distance_x = 85
    # Variablen zur Platzierung der Buttons der Liste Button2
    trapez_button_x = 450
    trapez_button_y = 200
    # Variable zur Bestimmung des verwendeten Entries
    eingabe_entry = 0

    ##INITIALISIERUNG FENSTER##
    def __init__(self, master):
        self.master = master
        master.title("Taschenrechner")
        master.geometry("700x650")

        self.formel_entry = None
        self.ergebnis_entry = None
        self.a_entry = None
        self.b_entry = None
        self.n_entry = None

        self.initEntries()
        self.initLabels()
        self.initButtons()

    ##FUNKTIONEN##
    def initEntries(self):
        # Initialize the formula and result entries
        formula_entry_width = 200
        result_entry_width = 100
        self.formel_entry = self.createAndPlaceEntry(self.formel_entry_x, self.eingabe_entry_y,
                                                     width=formula_entry_width)
        self.ergebnis_entry = self.createAndPlaceEntry(self.ergebnis_entry_x, self.eingabe_entry_y,
                                                       width=result_entry_width)

        # Initialize the trapezoidal sum entries
        trapez_width = 100
        trapez_offset = 125
        self.a_entry = self.createAndPlaceEntry(self.trapez_x, self.trapez_y, width=trapez_width)
        self.b_entry = self.createAndPlaceEntry(self.trapez_x + trapez_offset, self.trapez_y, width=trapez_width)
        self.n_entry = self.createAndPlaceEntry(self.trapez_x + 2 * trapez_offset, self.trapez_y, width=trapez_width)

    def initLabels(self):
        # Initialize the labels for the Trapezoidal Sum entries
        labels = [
            tk.Label(root, text="Startpunkt"),
            tk.Label(root, text="Endpunkt"),
            tk.Label(root, text="Anzahl Trapeze")
        ]

        # Initial label placement positions
        label_positions = [
            {'x': self.trapez_x, 'y': self.trapez_y - self.abstand_label},
            {'x': self.trapez_x + 125, 'y': self.trapez_y - self.abstand_label},
            {'x': self.trapez_x + 250, 'y': self.trapez_y - self.abstand_label}
        ]

        # Place the labels using a for loop
        for index, label in enumerate(labels):
            label.place(x=label_positions[index]['x'], y=label_positions[index]['y'])

        # Define and place the label for the equal sign
        equal_sign_label = tk.Label(root, text="=")
        equal_sign_label.place(x=self.formel_entry_x + 210, y=self.eingabe_entry_y - 3)

    def initButtons(self):
        # Configuration for standard calculator buttons
        BUTTON_WIDTH, BUTTON_HEIGHT = 10, 4

        buttons = [
            # Row 1
            {'text': 'AC', 'command': self.deleteAll},
            {'text': '/', 'command': lambda: self.taste_gedrueckt("/")},
            {'text': '*', 'command': lambda: self.taste_gedrueckt("*")},
            {'text': 'DEL', 'command': self.deleteLast},
            # Row 2
            {'text': '7', 'command': lambda: self.taste_gedrueckt("7")},
            {'text': '8', 'command': lambda: self.taste_gedrueckt("8")},
            {'text': '9', 'command': lambda: self.taste_gedrueckt("9")},
            {'text': '-', 'command': lambda: self.taste_gedrueckt("-")},
            # Row 3
            {'text': '4', 'command': lambda: self.taste_gedrueckt("4")},
            {'text': '5', 'command': lambda: self.taste_gedrueckt("5")},
            {'text': '6', 'command': lambda: self.taste_gedrueckt("6")},
            {'text': '+', 'command': lambda: self.taste_gedrueckt("+")},
            # Row 4
            {'text': '1', 'command': lambda: self.taste_gedrueckt("1")},
            {'text': '2', 'command': lambda: self.taste_gedrueckt("2")},
            {'text': '3', 'command': lambda: self.taste_gedrueckt("3")},
            {'text': '=', 'command': lambda: self.berechne()},
            # Row 5
            {'text': '%', 'command': lambda: self.taste_gedrueckt("%")},
            {'text': '0', 'command': lambda: self.taste_gedrueckt("0")},
            {'text': '.', 'command': lambda: self.taste_gedrueckt(".")},
            {'text': '^', 'command': lambda: self.taste_gedrueckt("^")}, ]

        for i, btn_info in enumerate(buttons):
            self.createButton(btn_info, i, BUTTON_WIDTH, BUTTON_HEIGHT, False)

        # Update coordinates for the next set of buttons
        self.y_button += 85
        self.x_button = 100

        # Configuration for special buttons
        BUTTON2_WIDTH, BUTTON2_HEIGHT = 3, 0

        buttons2 = [{'text': 'x', 'command': lambda: self.taste_gedrueckt("x")},
                    {'text': 'sqrt', 'command': lambda: self.spezialRechnungen("sqrt")},
                    {'text': 'log', 'command': lambda: self.spezialRechnungen("log")},
                    {'text': 'cos', 'command': lambda: self.spezialRechnungen("cos")},
                    {'text': 'sin', 'command': lambda: self.spezialRechnungen("sin")},
                    {'text': 'tan', 'command': lambda: self.spezialRechnungen("tan")},
                    {'text': '(', 'command': lambda: self.taste_gedrueckt("(")},
                    {'text': ')', 'command': lambda: self.taste_gedrueckt(")")}]
        self.button_distance_x /= 2
        for i, btn_info in enumerate(buttons2):
            self.createButton(btn_info, i, BUTTON2_WIDTH, BUTTON2_HEIGHT, True)

        # Initialize Trapez buttons
        self.initTrapezButtons()

    def initTrapezButtons(self):
        width = 20
        trapez_buttons = [{'text': 'TrapezSumme-Start', 'command': lambda: self.setEingabeEntry(1)},
                          {'text': 'TrapezSumme-Ende', 'command': lambda: self.setEingabeEntry(2)},
                          {'text': 'TrapezSumme-Zahl', 'command': lambda: self.setEingabeEntry(3)},
                          {'text': 'Rechner', 'command': lambda: self.setEingabeEntry(0)},
                          {'text': 'Trapez-Rechnung', 'command': self.trapezSumme}]

        for button_info in trapez_buttons:
            button = tk.Button(self.master, text=button_info['text'], command=button_info['command'], width=width)
            button.place(x=self.trapez_button_x, y=self.trapez_button_y)
            self.trapez_button_y += 50

    def createButton(self, btn_info, index, width, height, is_special):
        row_size = 4
        if not is_special:
            if index and index % row_size == 0:
                self.y_button += 75
                self.x_button = 100

        btn = tk.Button(self.master, text=btn_info['text'], command=btn_info['command'], width=width, height=height)
        btn.place(x=self.x_button, y=self.y_button)
        self.x_button += self.button_distance_x

    def createAndPlaceEntry(self, x, y, width=30):
        # Create a Tkinter Entry widget and place it on the screen at (x, y)
        entry = tk.Entry(self.master, width=width, justify="center")
        entry.place(x=x, y=y, width=width)
        return entry

    def spezialRechnungen(self, taste):
        if self.sqrt_log_cos_sin_tanStart == 1:
            self.sqrt_log_cos_sin_tanStart = 0
            self.formel_entry.insert("end", "]")
            eingabe = self.formel_entry.get()

            # Call the separated function and get the result and the length
            result, laenge = evaluate_special_operations(eingabe, taste)

            # Delete the function name and brackets based on the type of operation
            if taste in ["log", "cos", "sin", "tan"]:
                self.formel_entry.delete(laenge - 5, "end")
            elif taste == "sqrt":
                self.formel_entry.delete(laenge - 6, "end")

            # Insert the result into the formel_entry
            self.formel_entry.insert("end", result)

        else:
            self.sqrt_log_cos_sin_tanStart = 1
            if taste == "log":
                self.formel_entry.insert("end", "log[")
            elif taste == "cos":
                self.formel_entry.insert("end", "cos[")
            elif taste == "sin":
                self.formel_entry.insert("end", "sin[")
            elif taste == "tan":
                self.formel_entry.insert("end", "tan[")
            elif taste == "sqrt":
                self.formel_entry.insert("end", "sqrt[")

    def taste_gedrueckt(self, taste):
        # Funktion fügt durch Variable bestimmtes Entry gegebenes Symbol an. Symbol entspricht dem auf dem Knopf
        # angezeigten
        if self.eingabe_entry == 0:
            self.formel_entry.insert("end", taste)
        elif self.eingabe_entry == 1:
            self.a_entry.insert("end", taste)
        elif self.eingabe_entry == 2:
            self.b_entry.insert("end", taste)
        elif self.eingabe_entry == 3:
            self.n_entry.insert("end", taste)

    def berechne(self):
        try:
            self.formel_entry.config(background="white")
            # Ersetzte ^ mit ** für Potenzrechnung
            expression = self.formel_entry.get().replace('^', '**')
            # Berechne Funktion
            result = eval(expression)
            # Füge Ergebnis in Ergebnis Entry ein
            self.ergebnis_entry.delete(0, 'end')
            self.ergebnis_entry.insert('end', str(result))
        except ZeroDivisionError:
            self.formel_entry.config(background="red")
            self.ergebnis_entry.delete(0, 'end')
            self.ergebnis_entry.insert('end', "Cannot divide by zero")
        except Exception:
            self.formel_entry.config(background="red")
            self.ergebnis_entry.delete(0, 'end')
            self.ergebnis_entry.insert('end', "Error")

    def deleteLast(self):
        entry_map = {
            0: self.formel_entry,
            1: self.a_entry,
            2: self.b_entry,
            3: self.n_entry
        }

        current_entry = entry_map.get(self.eingabe_entry, None)

        if current_entry:
            current_entry.delete(len(current_entry.get()) - 1, "end")

    def deleteAll(self):
        entries_to_clear = [self.formel_entry, self.ergebnis_entry, self.a_entry, self.b_entry, self.n_entry]
        for entry in entries_to_clear:
            entry.config(background="white")
            entry.delete(0, "end")

    def setEingabeEntry(self, benutze_entry):
        self.eingabe_entry = benutze_entry

    def trapezSumme(self):
        # Clear the existing result from the entry field
        self.ergebnis_entry.delete(0, "end")

        try:
            # Get input values for trapezoidal sum calculation
            formula = self.formel_entry.get()
            a_value = int(self.a_entry.get())
            b_value = int(self.b_entry.get())
            n_value = int(self.n_entry.get())

            # Compute the trapezoidal sum using input values
            result = trapezSumme(formula, a_value, b_value, n_value)

            # Display the result
            self.ergebnis_entry.insert(0, result)

        except ValueError:
            # Handle invalid input (e.g., non-integer or empty values)
            self.ergebnis_entry.insert(0, "Invalid Input")

        except Exception as e:
            # Handle other exceptions
            self.ergebnis_entry.insert(0, "Error")
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Taschenrechner(master=root)
    root.mainloop()
