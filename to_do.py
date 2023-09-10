import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task!")

def edit_task():
    selected_index = task_list.curselection()
    if selected_index:
        selected_task = task_list.get(selected_index)
        edit_window = tk.Toplevel(root)

        def save_changes():
            new_task = edit_entry.get()
            if new_task:
                task_list.delete(selected_index)
                task_list.insert(selected_index, new_task)
                edit_window.destroy()
            else:
                messagebox.showwarning("Empty Task", "Please enter a task!")

        edit_label = tk.Label(edit_window, text="Edit Task:", font=("Arial", 12, "bold"))
        edit_label.pack(pady=10)
        edit_entry = tk.Entry(edit_window, font=("Arial", 12))
        edit_entry.pack()
        edit_entry.insert(tk.END, selected_task)
        save_button = tk.Button(edit_window, text="Save Changes", font=("Arial", 12, "bold"), command=save_changes)
        save_button.pack(pady=10)

    else:
        messagebox.showwarning("No Task Selected", "Please select a task to edit!")

def delete_task():
    selected_index = task_list.curselection()
    if selected_index:
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?")
        if confirm:
            task_list.delete(selected_index)
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete!")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(background="sky blue")

task_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.SOLID)
task_frame.pack(pady=20)

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(task_frame, width=35, height=10, font=("Arial", 12), yscrollcommand=scrollbar.set, bd=0, relief=tk.FLAT)
task_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=task_list.yview)

task_entry = tk.Entry(root, width=35, font=("Arial", 14), bd=2, relief=tk.SOLID)
task_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", background="white", font=("Arial", 15, "bold"), command=add_task, bd=2, relief=tk.SOLID)
add_button.pack(side=tk.LEFT, padx=5)

edit_button = tk.Button(button_frame, text="Edit Task", background="white", font=("Arial", 15, "bold"), command=edit_task, bd=2, relief=tk.SOLID)
edit_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", background="white", font=("Arial", 15, "bold"), command=delete_task, bd=2, relief=tk.SOLID)
delete_button.pack(side=tk.LEFT, padx=5)

root.mainloop()