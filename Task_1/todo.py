import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set the width and height of the main window
root.geometry("300x300")  # Adjust width and height as needed

# Create an entry widget for adding tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

# Create a button to remove tasks
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Run the main loop
root.mainloop()
