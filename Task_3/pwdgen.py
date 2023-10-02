import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user preferences
    all_chars = upper_letters + lower_letters + digits + special_chars

    # Ensure the password length is between 8 and 16 characters
    length = max(8, min(length, 16))

    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def generate_password_gui():
    try:
        # Get the desired password length from the user input field
        length = int(length_entry.get())

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Please enter a valid number for the password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a style for the GUI elements
style = ttk.Style()
style.configure('TButton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 14))
style.configure('TEntry', font=('Arial', 14))

# Label and entry field for password length
length_label = ttk.Label(root, text="Enter the desired password length (8-16):")
length_label.pack(pady=10)

length_entry = ttk.Entry(root)
length_entry.pack(pady=5)

# Button to generate password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=10)

# Label to display the generated password
result_label = ttk.Label(root, text="", foreground="blue")
result_label.pack(pady=10)

# Center the window on the screen
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# Run the GUI
root.mainloop()
