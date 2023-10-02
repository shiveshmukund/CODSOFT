import tkinter as tk
import os

# Function to perform mathematical operations
def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operation = operation_var.get()

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            result_label.config(text="Cannot divide by zero")
            return
        result = num1 / num2
    else:
        result_label.config(text="Invalid operation")
        return

    result_label.config(text=f"Result: {result:.2f}")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Increase the width of the window
root.geometry("400x300")  # Width x Height

# Create and set up widgets
operation_var = tk.StringVar()
operation_var.set("Addition")

title_label = tk.Label(root, text="Simple Calculator", font=("Helvetica", 16))
title_label.pack(pady=10)

num1_label = tk.Label(root, text="Enter first number:")
num1_label.pack()

num1_entry = tk.Entry(root, width=20)  # Increase width
num1_entry.pack()

num2_label = tk.Label(root, text="Enter second number:")
num2_label.pack()

num2_entry = tk.Entry(root, width=20)  # Increase width
num2_entry.pack()

operation_label = tk.Label(root, text="Select operation:")
operation_label.pack()

operations = ["Addition", "Subtraction", "Multiplication", "Division"]

operation_option_menu = tk.OptionMenu(root, operation_var, *operations)
operation_option_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()
