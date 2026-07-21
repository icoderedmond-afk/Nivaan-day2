import random

def get_choices():
  player_choice = input("ENTER a choice(rock, paper, scissors: ").lower() 
  options = ["rock", "paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
  
def check_win(player, computer):
    print(f"you chose {player}, computer chose  {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smahes scissors! You win!"
        else:
            return "Paper cover rock!Yous lose"
    elif player == "paper":
        if computer =="rock":
            return "Rock covers rock you win!"
        else:
            return "Paper covers rock! You lose."

    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors!You lose" 
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)