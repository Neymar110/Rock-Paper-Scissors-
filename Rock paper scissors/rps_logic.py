import random

def bot_choice_generator():
    choices = ["rock", "paper", "scissors"]
    num = random.randint(0, 2)
    return choices[num]
def input_validation(answer):
    valid = False
    while not valid:
        if (answer == "rock") or (answer == "paper") or (answer == "scissors") or (answer == "Scissors") or (answer == "Paper") or (answer == "Rock"):
            valid = True
        else:
            print("That is not a valid choice")
            answer = input("Rock, Paper or Scissors? ")
    return answer


def logic(user, bot):
    if bot == "rock" and user == "paper":
        return True
    elif bot == "rock" and user == "scissors":
        return False
    elif bot == "paper" and user == "scissors":
        return True
    elif bot == "paper" and user == "rock":
        return False
    elif bot == "scissors" and user == "rock":
        return True
    elif bot == "scissors" and user == "paper":
        return False

def best_of_one(users_input):
    score = []
    users_input = input_validation(users_input).lower()
    bots_choice = bot_choice_generator() 
    if logic(users_input, bots_choice):
        score.append(f"won")
    elif bots_choice == users_input:
        score.append(f"drawed")
    else:
        score.append(f"lost")
    return score
