import xbmcgui
import xbmcplugin
import xbmcaddon
import sys

addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')
addon_handle = int(sys.argv[1])

def calculator():
    try:
        # Show dialog to enter the first number
        first_number = xbmcgui.Dialog().input("Enter First Number", type=xbmcgui.INPUT_NUMERIC)
        if first_number == "":
            return

        # Show dialog to select operation
        operations = ['Addition (+)', 'Subtraction (-)', 'Multiplication (*)', 'Division (/)']
        selected_operation = xbmcgui.Dialog().select("Select Operation", operations)
        if selected_operation == -1:
            return

        # Show dialog to enter the second number
        second_number = xbmcgui.Dialog().input("Enter Second Number", type=xbmcgui.INPUT_NUMERIC)
        if second_number == "":
            return

        # Perform the selected operation
        first_number = float(first_number)
        second_number = float(second_number)
        result = 0

        if selected_operation == 0:  # Addition
            result = first_number + second_number
        elif selected_operation == 1:  # Subtraction
            result = first_number - second_number
        elif selected_operation == 2:  # Multiplication
            result = first_number * second_number
        elif selected_operation == 3:  # Division
            if second_number != 0:
                result = first_number / second_number
            else:
                xbmcgui.Dialog().ok("Error", "Division by zero is not allowed.")
                return

        # Show the result in a dialog
        xbmcgui.Dialog().ok("Result", f"The result is: {result}")

    except ValueError:
        xbmcgui.Dialog().ok("Error", "Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
