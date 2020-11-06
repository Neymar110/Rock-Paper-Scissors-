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
    draw = f"Master minds. You both played {users_input}"
    win = f"Well Done! You played {users_input}, and the bot played {bots_choice}."
    lose = f"Uh oh, You played {users_input} and the bot played {bots_choice}."
    if logic(users_input, bots_choice):
        result = win
        score.append(f"{users_input} : win")
    elif bots_choice == users_input:
        result = draw
        score.append(f"{users_input} : draw")
    else:
        result = lose
        score.append(f"{users_input} : lose")
    final_return = [result, score]
    return final_return

# def best_of_five(users_input): 
#     score = []
#     count = 0
#     while count < 5:
#         users_input = input_validation(users_input)
#         bots_choice = bot_choice_generator() 
#         draw = f"Master minds. You both played {users_input}"
#         win = f"Well Done! You played {users_input}, and the bot played {bots_choice}."
#         lose = f"Uh oh, You played {users_input} and the bot played {bots_choice}."
#         if logic(users_input, bots_choice):
#             print(win)
#             score.append(f"{users_input} : win")
#         elif bots_choice == users_input:
#             print(draw)
#             score.append(f"{users_input} : draw")
#         else:
#             print(lose)
#             score.append(f"{users_input} : lose")
#         count += 1
#     print(score)

# def best_of_three(users_choice):
#     score = []
#     count = 0
#     while count < 3:
#         users_choice = input_validation(users_choice)
#         bots_choice = bot_choice_generator() 
#         draw = f"Master minds. You both played {bots_choice}"
#         win = f"Well Done! You played {users_choice}, and the bot played {users_choice}."
#         lose = f"Uh oh, You played {users_choice} and the bot played {bots_choice}."
#         if logic(users_choice, bots_choice):
#             print(win)
#             score.append(f"{users_choice} : win")
#         elif bots_choice == users_choice:
#             print(draw)
#             score.append(f"{users_choice} : draw")
#         else:
#             print(lose)
#             score.append(f"{users_choice} : lose")
#         count += 1
#     print(score)

# def initiation_func(rounds):
#     if rounds == "1" or rounds == "one":
#         return best_of_one()
    
#     elif rounds == "3" or rounds == "three":
#         return best_of_three()
    
#     elif rounds == "5" or rounds == "five":
#         return best_of_five()

# def init(users_input):
#     score = []
#     count = 0
#     a = best_of_one
#     while count < rounds:
#         count += 1
#         score.append(a(users_input))
