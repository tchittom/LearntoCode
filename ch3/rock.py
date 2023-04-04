import random

def generate_choice():
    choice = random.randint(0,2)
    if choice == 0:
        return "rock"
    elif choice == 1:
        return "paper"
    else:
        return "scissors"

def winner(player_choice, computer_choice):
    if player_choice == "rock" and computer_choice == "rock":
        return "It was a tie!"
    elif player_choice == "rock" and computer_choice == "paper":
        return "P2 wins!"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "P1 wins!"
    
def play_rock_paper_scissors():
  player_choice = input("choose rock, paper, or scissors: ")
  computer_choice = generate_choice()
  print("Player chose: ", player_choice)
  print("Computer chose: ", computer_choice)
  if validate(player_choice):
        return winner(player_choice, computer_choice)
  else:
    print("Invalid Selection.  Please select rock, paper, or scissors")
    return play_rock_paper_scissors()

def validate(choice):
    available_options = ["rock", "paper", "scissors"]
    if choice in available_options:
        return True
    else:
        return False

Print(play_rock_paper_scissors())
