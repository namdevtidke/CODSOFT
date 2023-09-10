import tkinter as tk
import random
import string

def generate_password():
    password_length = length_slider.get()
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    password_characters = ''
    if include_lowercase:
        password_characters += string.ascii_lowercase
    if include_uppercase:
        password_characters += string.ascii_uppercase
    if include_digits:
        password_characters += string.digits
    if include_special_chars:
        password_characters += string.punctuation

    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

window = tk.Tk()
window.title("Password Generator")
window.configure(background="#f1f1f1")

length_label = tk.Label(window, text="Password Length:", background="#f1f1f1", font=("Arial", 16))
length_label.pack()

length_slider = tk.Scale(window, from_=8, to=25, orient=tk.HORIZONTAL, background="#f1f1f1", font=("Arial", 16), length=300)
length_slider.pack()

lowercase_var = tk.IntVar()
lowercase_check = tk.Checkbutton(window, text="Include Lowercase", background="#f1f1f1", variable=lowercase_var, font=("Arial", 16))
lowercase_check.pack()

uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(window, text="Include Uppercase", background="#f1f1f1", variable=uppercase_var, font=("Arial", 16))
uppercase_check.pack()

digits_var = tk.IntVar()
digits_check = tk.Checkbutton(window, text="Include Digits", background="#f1f1f1", variable=digits_var, font=("Arial", 16))
digits_check.pack()

special_chars_var = tk.IntVar()
special_chars_check = tk.Checkbutton(window, text="Include Special Characters", background="#f1f1f1", variable=special_chars_var, font=("Arial", 16))
special_chars_check.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password, background="#007bff", fg="black", font=("Arial", 16), padx=10, pady=10)
generate_button.pack()

length_label1 = tk.Label(window, text="Your generated password is:", background="#f1f1f1", font=("Arial", 16))
length_label1.pack()

password_entry = tk.Entry(window, width=30, font=("Arial", 16))
password_entry.pack(padx=20, pady=20)


window.option_add("*Font", "Arial 18")
window.option_add("*Button.Background", "#007bff")
window.option_add("*Button.Foreground", "white")
window.option_add("*Button.Relief", "raised")

window.mainloop()