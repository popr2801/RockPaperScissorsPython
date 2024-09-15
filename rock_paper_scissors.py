import tkinter as tk
parent = tk.Tk()
score_var = tk.IntVar()
def update_score():
    score = score_var.get()
    score+=1
    score_var.set(score)
    score_label.config(text = score)

parent.geometry("400x400")
score_label = tk.Label(parent,text = score_var.get())
score_label.pack(side = "left")
score_button = tk.Button(parent,text = "Click Me",command = update_score)
score_button.pack(side = "right")


parent.mainloop()