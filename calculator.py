import tkinter as tk
from math import sqrt

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Division by zero")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_decimal():
    current = entry.get()
    if '.' not in current:
        entry.insert(tk.END, '.')

def button_square_root():
    try:
        result = sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Invalid input")

def button_backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def button_negate():
    current = entry.get()
    if current and current[0] == '-':
        entry.delete(0)
    else:
        entry.insert(0, '-')

window = tk.Tk()
window.title("Calculator")
window.configure(background="white")

entry = tk.Entry(window, width=30, font=("Arial", 19))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = []
for i in range(9, 0, -1):
    button = tk.Button(window, text=str(i), padx=20, pady=10, font=("Arial", 16), command=lambda num=i: button_click(num))
    buttons.append(button)

button_0 = tk.Button(window, text="0", padx=20, pady=10, font=("Arial", 16), command=lambda: button_click(0))
button_decimal = tk.Button(window, text=".", padx=20, pady=10, font=("Arial", 16), command=button_decimal)

button_add = tk.Button(window, text="+", padx=20, pady=10, font=("Arial", 16), command=lambda: button_click('+'))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, font=("Arial", 16), command=lambda: button_click('-'))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, font=("Arial", 16), command=lambda: button_click('*'))
button_divide = tk.Button(window, text="/", padx=20, pady=10, font=("Arial", 16), command=lambda: button_click('/'))
button_equal = tk.Button(window, text="=", padx=20, pady=10, font=("Arial", 16), command=button_equal)
button_clear = tk.Button(window, text="C", padx=20, pady=10, font=("Arial", 16), background="red", command=button_clear)
button_decimal=tk.Button(window, text=".", padx=20, pady=10, font=("Arial", 16), command=lambda: button_click('.'))
button_square_root = tk.Button(window, text="√", padx=20, pady=10, font=("Arial", 16), command=button_square_root)
button_backspace = tk.Button(window, text="←", padx=20, pady=10, font=("Arial", 16), command=button_backspace)
button_negate = tk.Button(window, text="+/-", padx=20, pady=10, font=("Arial", 16), command=button_negate)

row_index = 2
col_index = 0

for i, button in enumerate(buttons):
    button.grid(row=row_index, column=col_index, padx=5, pady=5)
    col_index += 1
    if col_index > 2:
        col_index = 0
        row_index += 1

button_0.grid(row=row_index, column=col_index, padx=5, pady=5)
button_decimal.grid(row=row_index, column=col_index+1, padx=5, pady=5)

button_add.grid(row=2, column=3, padx=5, pady=5)
button_subtract.grid(row=3, column=3, padx=5, pady=5)
button_multiply.grid(row=4, column=3, padx=5, pady=5)
button_divide.grid(row=5, column=3, padx=5, pady=5)
button_equal.grid(row=5, column=2, padx=5, pady=5)
button_clear.grid(row=1, column=3, padx=5, pady=5)
button_decimal.grid(row=5, column=1, padx=5, pady=5)
button_square_root.grid(row=1, column=1, padx=5, pady=5)
button_backspace.grid(row=1, column=2, padx=5, pady=5)
button_negate.grid(row=1, column=0, padx=5, pady=5)

window.option_add("*Font", "Arial 12")
window.option_add("*Button.Background", "black")
window.option_add("*Button.Foreground", "white")
window.option_add("*Button.Relief", "groove")

window.mainloop()