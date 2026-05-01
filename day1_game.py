import random

#game of rock paper scissors
def get_choice():
    # user_choice="rock"
    user_choice=input("Enter your choice (rock, paper, scissors):  ")
    # The above line prompts the user to input their choice for the game. The input() function displays the message "Enter your choice (rock, paper, scissors): " and waits for the user to type something and press Enter. The user's input is then stored in the variable user_choice.
    
    # computer_choice="Paper"
    computer_choice=random.choice(["rock","paper","scissors"])
    #in the above line, random.choice() is a function from the random module that selects a random item from the provided list ["rock", "paper", "scissors"]. This simulates the computer's choice in the game.
    
    choices_dict={"user":user_choice,"computer":computer_choice}
    return choices_dict
# store_choice=get_choice()
# print(store_choice)

def check_winner(user ,computer):
    print(f"You chose: {user} | Computer chose: {computer}")
    if user == computer:
        return "It's a tie!"
    elif user=="rock":
        if computer=="scissors":
            return "You win!"
        else:
            return "Computer wins!"
    elif user=="paper":
        if computer=="rock":
            return "You win!"
        else:
            return "Computer wins!"
    elif user=="scissors":
        if computer=="paper":
            return "You win!"
        else:
            return "Computer wins!"
    
choice=get_choice()
result=check_winner(choice["user"], choice["computer"])
print(result)
