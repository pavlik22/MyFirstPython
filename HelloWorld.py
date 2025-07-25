def add(x, y):
    return x + y

def subtract(x, y):
    return x - y



# Simple Calculator GUI with number buttons using tkinter
import tkinter as tk
from tkinter import messagebox

selected_numbers = []

def select_number(n):
    if len(selected_numbers) < 2:
        selected_numbers.append(n)
        update_selected_display()
    else:
        messagebox.showinfo("Info", "Only two numbers can be selected.")

def clear_selection():
    selected_numbers.clear()
    update_selected_display()
    result_var.set("")

def update_selected_display():
    if len(selected_numbers) == 0:
        selected_var.set("Selected: ")
    elif len(selected_numbers) == 1:
        selected_var.set(f"Selected: {selected_numbers[0]}")
    else:
        selected_var.set(f"Selected: {selected_numbers[0]}, {selected_numbers[1]}")

def handle_add():
    if len(selected_numbers) == 2:
        x, y = selected_numbers
        result = add(x, y)
        result_var.set(f"Result: {x} + {y} = {result}")
    else:
        messagebox.showerror("Input Error", "Please select two numbers.")

def handle_subtract():
    if len(selected_numbers) == 2:
        x, y = selected_numbers
        result = subtract(x, y)
        result_var.set(f"Result: {x} - {y} = {result}")
    else:
        messagebox.showerror("Input Error", "Please select two numbers.")

root = tk.Tk()
root.title("Simple Calculator")

selected_var = tk.StringVar()
selected_var.set("Selected: ")
selected_label = tk.Label(root, textvariable=selected_var, font=("Arial", 12))
selected_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Number buttons (0-9)
for i in range(10):
    btn = tk.Button(root, text=str(i), width=5, height=2, command=lambda n=i: select_number(n))
    btn.grid(row=1 + i // 5, column=i % 5, padx=5, pady=5)

tk.Button(root, text="Clear", width=10, command=clear_selection).grid(row=3, column=4, padx=10, pady=10)

tk.Button(root, text="Add", width=10, command=handle_add).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", width=10, command=handle_subtract).grid(row=4, column=1, padx=10, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

root.mainloop()
