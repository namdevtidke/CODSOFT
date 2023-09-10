import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class QuizGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MCQ Quiz")
        self.master.geometry("600x400")
        
        self.questions = [
            {
                "question": "What is the maximum possible length of an identifier in python?",
                "options": ["16", "32", "64", "none of the above"],
                "answer": 4
            },
            {
                "question": "Who developed the Python language? ",
                "options": ["Zim Den", "Guido van Rossum", "Niene Stom", "Wick van Rossum"],
                "answer": 2
            },
            {
                "question": "In which language is Python written?",
                "options": ["English", "PHP", "C", "All of the above"],
                "answer": 3
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 18))
        
        self.question_label = ttk.Label(master, text="")
        self.question_label.pack(pady=20)
        
        self.option_var = tk.IntVar()
        
        self.option_radios = []
        for i in range(4):
            radio = ttk.Radiobutton(master, text="", variable=self.option_var, value=i)
            radio.pack(anchor=tk.W)
            self.option_radios.append(radio)
        
        self.submit_button = ttk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
        
        self.score_label = ttk.Label(master, text="")
        self.score_label.pack()
        
        self.show_question()
        
    def show_question(self):
        question_data = self.questions[self.current_question]
        
        self.question_label.config(text=question_data["question"])
        
        for i, option_radio in enumerate(self.option_radios):
            option_radio.config(text=question_data["options"][i])
        
        self.option_var.set(-1) 
        
        self.submit_button.config(state=tk.NORMAL) 
        
        self.score_label.config(text=f"Score: {self.score}/{self.current_question}")
    
    def check_answer(self):
        selected_option = self.option_var.get()
        correct_answer = self.questions[self.current_question]["answer"]
        
        if selected_option == -1:
            messagebox.showwarning("No Option Selected", "Please select an option.")
            return
        
        if selected_option == correct_answer:
            self.score += 1
        
        self.submit_button.config(state=tk.DISABLED)  
        
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Finished", f"You have answered all the questions!\nYour score: {self.score}/{len(self.questions)}")
            self.master.destroy()  

root = tk.Tk()

quiz = QuizGUI(root)

root.mainloop()