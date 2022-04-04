from tkinter import *
from tkinter.font import *
import random, time

items=[
"Rock",
"Paper",
"Scissors",
]

player_choice = ""
computer_choice = ""

def start_game():

    try:
        welcome_window.destroy()

    except:
        pass

    game_window = Tk()

    game_window.title("Rock Paper Scissors Game")

    game_window.configure(bg="black")

    game_window.iconbitmap("game_controller.ico")

    game_window.resizable(False, False)

    game_window.eval("tk::PlaceWindow . center")

    game_window.geometry("-340+300")

    def reset_game():

        game_window.destroy()

        start_game()

    def rock():
        global player_choice

        player_label.configure(text="Rock")

        computer_label.configure(text="Computer")

        player_choice = "Rock"

    def paper():
        global player_choice

        player_label.configure(text="Paper")

        computer_label.configure(text="Computer")

        player_choice = "Paper"

    def scissors():
        global player_choice

        player_label.configure(text="Scissors")

        computer_label.configure(text="Computer")

        player_choice = "Scissors"

    def go():
        global player_choice
        global computer_choice

        computer_choice = random.choice(items)

        computer_label.configure(text = computer_choice)

        if player_choice == computer_choice:

            game_result.configure(text = "Draw!")

        elif player_choice == "Rock" and computer_choice == "Paper":

            game_result.configure(text = "You Lose!")

        elif player_choice == "Rock" and computer_choice == "Scissors":

            game_result.configure(text = "You Win!")

        elif player_choice == "Paper" and computer_choice == "Rock":

            game_result.configure(text="You Win!")

        elif player_choice == "Paper" and computer_choice == "Scissors":

            game_result.configure(text="You Lose!")

        elif player_choice == "Scissors" and computer_choice == "Rock":

            game_result.configure(text="You Lose!")

        elif player_choice == "Scissors" and computer_choice == "Paper":

            game_result.configure(text="You Win!")

        game_result.grid(row=3, column=1, padx=40, pady=40, ipadx=10, ipady=10)

    Label(text="Rock Paper Scissors Game", font=("Consolas", 18, BOLD), fg="white", bg="black").grid(row=0, column=1, pady=20, sticky="E")

    player_label = Label(text="You", font=("Consolas", 18, BOLD), fg = "white", bg="black")
    player_label.grid(row=1, column=0, pady=5)

    Label(text="VS.", font=("Consolas", 18, BOLD), fg = "white", bg="black").grid(row=1, column=1, pady=5)

    computer_label = Label(text="Computer", font=("Consolas", 18, BOLD), fg = "white", bg="black")
    computer_label.grid(row=1, column=2, pady=5)

    Button(game_window, text="Rock", command=rock, font=("Consolas", 18, BOLD), bg = "#9ED8DB", activebackground="#51989c", relief="flat", fg="black").grid(row=2, column=0, padx=40, pady=40, ipadx=10, ipady=10, sticky="E")
    Button(game_window, text="Paper", command=paper, font=("Consolas", 18, BOLD), bg = "#9ED8DB", activebackground="#51989c", relief="flat", fg="black").grid(row=2, column=1, padx=40, pady=40, ipadx=10, ipady=10)
    Button(game_window, text="Scissors", command=scissors, font=("Consolas", 18, BOLD), bg = "#9ED8DB", activebackground="#51989c", relief="flat", fg="black").grid(row=2, column=2, padx=40, pady=40, ipadx=10, ipady=10)

    game_result = Label(game_window, text="", font=("Consolas", 18, BOLD), bg = "black", fg="white")

    Button(game_window, text="      GO      ", command=go, font=("Consolas", 18, BOLD), bg = "#9ED8DB", activebackground="#51989c", relief="flat", fg="black").grid(row=4, column=1, padx=40, pady=40, ipadx=10, ipady=10)
    Button(game_window, text="RESET GAME", command=reset_game, font=("Consolas", 18, BOLD), bg = "#9ED8DB", activebackground="#51989c", relief="flat", fg="black").grid(row=4, column=2, padx=40, pady=40, ipadx=10, ipady=10)
    Button(game_window, text="QUIT GAME", command=exit, font=("Consolas", 18, BOLD), bg = "#9ED8DB", activebackground="#51989c", relief="flat", fg="black").grid(row=4, column=0, padx=40, pady=40, ipadx=10, ipady=10)

    game_window.mainloop()

welcome_window = Tk()

welcome_window.title("Welcome Screen")

welcome_window.iconbitmap('game_controller.ico')

welcome_window.configure(bg="black")

welcome_window.resizable(False, False)

welcome_window.eval("tk::PlaceWindow . center")

welcome_window.geometry("-280+280")

Label(text="Welcome to my Rock Paper Scissors Game", bg='black', fg='white', font=('Consolas', 15, BOLD)).pack(padx=15, pady=15, ipady=5, ipadx=5)
Label(text="This is a simple game I made using Tkinter", bg='black', fg='white', font=('Consolas', 15, BOLD)).pack(padx=15, pady=15, ipady=5, ipadx=5)
Label(text="The basic premise of the game is to play rock paper scissors against the computer", bg='black', fg='white', font=('Consolas', 15, BOLD)).pack(padx=15, pady=15, ipady=5, ipadx=5)
Label(text="Wether you win or not is completely up to chance", bg='black', fg='white', font=('Consolas', 15, BOLD)).pack(padx=15, pady=15, ipady=5, ipadx=5)
Label(text="Have fun!", bg='black', fg='white', font=('Consolas', 15, BOLD)).pack(padx=15, pady=15, ipady=5, ipadx=5)
Button(text="Start", command=start_game, font=('Consolas', 22, BOLD), bg="#9ED8DB", activebackground="#51989c", fg="black", relief="flat").pack(padx=10, pady=10)


welcome_window.mainloop()
