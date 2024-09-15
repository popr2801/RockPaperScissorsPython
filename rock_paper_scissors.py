import tkinter as tk, random


parent = tk.Tk()
score_var = tk.StringVar()


parent.geometry("600x400")
parent.rowconfigure(0,weight = 1)
parent.rowconfigure(2,weight = 1)
parent.columnconfigure(0,weight = 1)
parent.columnconfigure(1,weight = 1)
parent.columnconfigure(2,weight = 1)
"Opponent's Hand"
def randomHand():
    wordList = ["Rock","Paper","Scissors"]
    return wordList[random.randint(0,2)]


'Score Counting'
wins_var = tk.IntVar()
draws_var = tk.IntVar()
loses_var = tk.IntVar()
wins = wins_var.get()
draws = draws_var.get()
loses = loses_var.get()

def update_label(arg):
    global wins,draws,loses
    if arg == 1:
        wins += 1
    elif arg == 0:
        loses += 1
    scoreLabel.config(text = f"Wins: {wins}    Draws: {draws}    Loses: {loses}",)
    

'Button Section'
current_hand = None
oppHand = None
def chosenHand(button_name):
    global wins,draws,loses
    current_hand = button_name
    oppHand = randomHand()
    print(f"Your hand is:{current_hand}")
    print(f"Opponent's hand is:{oppHand}")
    if current_hand == 'Rock':
        if oppHand == 'Paper':
            print("You Lose!")
            update_label(0)
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nYou Lose!")
        elif oppHand == 'Scissors':
            print("You Win!")
            update_label(1)
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nYou Win!")
        else:
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nIt's A Draw!")
            print("It's A Draw!")
            draws += 1
    if current_hand == 'Paper':
        if oppHand == 'Scissors':
            print("You Lose!")
            update_label(0)
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nYou Lose!")
        elif oppHand == 'Rock':
            print("You Win!")
            update_label(1)
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nYou Win!")
        else:
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nIt's A Draw!")
            print("It's A Draw!")
            draws += 1
    if current_hand == 'Scissors':
        if oppHand == 'Rock':
            print("You Lose!")
            update_label(0)
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nYou Lose!")
        elif oppHand == 'Paper':
            print("You Win!")
            update_label(1)
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nYou Win!")
        else:
            resultsLabel.config(text = f"Opponent's hand is: {oppHand}\nIt's A Draw!")
            print("It's A Draw!")
            draws += 1
    scoreLabel.config(text = f"Wins: {wins}    Draws: {draws}    Loses: {loses}",)

resultsLabel = tk.Label(parent,text = " ")
scoreLabel = tk.Label(parent,text = f"Wins: {wins}    Draws: {draws}    Loses: {loses}")
rockButton = tk.Button(parent,text = "Rock",command = lambda: chosenHand("Rock"),width = 100)
paperButton = tk.Button(parent,text = "Paper",command = lambda: chosenHand("Paper"),width = 100)
scissorsButton = tk.Button(parent,text = "Scissors",command = lambda: chosenHand("Scissors"),width = 100)

rockButton.grid(row = 2, column = 0,padx = 10,sticky='ew')
paperButton.grid(row = 2, column = 1,padx = 10,sticky='ew')
scissorsButton.grid(row = 2, column = 2,padx = 10,sticky='ew')
scoreLabel.grid(row = 0, column = 0,sticky = 'nw')
resultsLabel.grid(row = 1,column = 1,pady = 10)





parent.mainloop()
