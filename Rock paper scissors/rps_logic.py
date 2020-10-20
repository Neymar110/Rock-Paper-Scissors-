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

    
def best_of_one():
    score = []
    user_input = input("Rock, Paper or Scissors? ").lower()
    user_input = input_validation(user_input)
    choice = bot_choice_generator() 
    draw = f"Master minds. You both played {choice}"
    win = f"Well Done! You played {user_input}, and the bot played {choice}."
    lose = f"Uh oh, You played {user_input} and the bot played {choice}."
    if logic(user_input, choice):
        print(win)
        score.append(f"{user_input} : win")
    elif choice == user_input:
        print(draw)
        score.append(f"{user_input} : draw")
    else:
        print(lose)
        score.append(f"{user_input} : lose")
    
    print(score)

def best_of_five(): 
    score = []
    count = 0
    while count < 5:
        user_input = input("Rock, Paper or Scissors? ").lower()
        user_input = input_validation(user_input)
        choice = bot_choice_generator() 
        draw = f"Master minds. You both played {choice}"
        win = f"Well Done! You played {user_input}, and the bot played {choice}."
        lose = f"Uh oh, You played {user_input} and the bot played {choice}."
        if logic(user_input, choice):
            print(win)
            score.append(f"{user_input} : win")
        elif choice == user_input:
            print(draw)
            score.append(f"{user_input} : draw")
        else:
            print(lose)
            score.append(f"{user_input} : lose")
        count += 1
    print(score)

def best_of_three():
    score = []
    count = 0
    while count < 3:
        user_input = input("Rock, Paper or Scissors? ").lower()
        user_input = input_validation(user_input)
        choice = bot_choice_generator() 
        draw = f"Master minds. You both played {choice}"
        win = f"Well Done! You played {user_input}, and the bot played {choice}."
        lose = f"Uh oh, You played {user_input} and the bot played {choice}."
        if logic(user_input, choice):
            print(win)
            score.append(f"{user_input} : win")
        elif choice == user_input:
            print(draw)
            score.append(f"{user_input} : draw")
        else:
            print(lose)
            score.append(f"{user_input} : lose")
        count += 1
    print(score)

best_of_what = int(input("How many rounds would you like to play? [1, 3, 5] "))
if best_of_what == 1:
    best_of_one()
elif best_of_what == 3:
    best_of_three()
elif best_of_what == 5:
    best_of_five()