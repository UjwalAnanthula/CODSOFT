import random
import tkinter as tk
from tkinter import messagebox

# Function to handle the game logic
def play(choice):
    global user_score, computer_score

    # Computer's random choice
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    # Logic to Determine the winner
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Scissors" and computer_choice == "Paper") or \
         (choice == "Paper" and computer_choice == "Rock"):
        result = "You won the round!"
        user_score += 1
    else:
        result = "You lose the round!"
        computer_score += 1

    # To Update scores and display results
    result_label.config(
        text=f"Your choice: {choice}\nComputer's choice: {computer_choice}\n{result}"
    )
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice to start the game!")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Initialize scores
user_score = 0
computer_score = 0

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x400")

# Instructions
instructions = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors to play against the computer!",
    font=("Arial", 20),
    wraplength=350,
)
instructions.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("Rock"), width=10)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("Paper"), width=10)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("Scissors"), width=10)
scissors_button.grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(root, text="Make your choice to start the game!", font=("Arial", 15))
result_label.pack(pady=20)

# Score display
score_label = tk.Label(root, text="- - - Score - You: 0 | Computer: 0 - - -", font=("Arial", 13))
score_label.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game, width=18)
reset_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
