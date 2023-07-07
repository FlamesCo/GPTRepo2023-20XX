import tkinter as tk
from tkinter import messagebox
import math

def calculate(operation):
    try:
        if operation == 'add':
            result = float(num1_entry.get()) + float(num2_entry.get())
        elif operation == 'subtract':
            result = float(num1_entry.get()) - float(num2_entry.get())
        elif operation == 'multiply':
            result = float(num1_entry.get()) * float(num2_entry.get())
        elif operation == 'divide':
            result = float(num1_entry.get()) / float(num2_entry.get())
        elif operation == 'square':
            result = float(num1_entry.get()) ** 2
        elif operation == 'sqrt':
            result = math.sqrt(float(num1_entry.get()))
        result_label.config(text=str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("GUI Calculator")

num1_entry = tk.Entry(root)
num1_entry.pack()

num2_entry = tk.Entry(root)
num2_entry.pack()

add_button = tk.Button(root, text="Add", command=lambda: calculate('add'))
add_button.pack()

subtract_button = tk.Button(root, text="Subtract", command=lambda: calculate('subtract'))
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=lambda: calculate('multiply'))
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=lambda: calculate('divide'))
divide_button.pack()

square_button = tk.Button(root, text="Square", command=lambda: calculate('square'))
square_button.pack()

sqrt_button = tk.Button(root, text="Square Root", command=lambda: calculate('sqrt'))
sqrt_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
