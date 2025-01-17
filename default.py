import xbmc
import xbmcgui

class Calculator:
    def __init__(self):
        self.result = ""

    def input(self, value):
        self.result += str(value)

    def calculate(self):
        try:
            # Evaluate the expression safely
            self.result = str(eval(self.result))
        except Exception:
            self.result = "Error"

    def clear(self):
        self.result = ""

    def show(self):
        dialog = xbmcgui.Dialog()
        while True:
            # Create a list of buttons for the calculator
            buttons = ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", "0", "C", "=", "Exit"]
            button = dialog.select("Calculator", buttons)
            if button == -1 or button == 15:  # Exit
                break
            elif button == 12:  # Clear
                self.clear()
            elif button == 13:  # Equals
                self.calculate()
            else:
                self.input(buttons[button])
            # Show the current result after each input
            dialog.ok("Result", self.result)

if __name__ == "__main__":
    calc = Calculator()
    calc.show()
