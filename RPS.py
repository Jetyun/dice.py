# rock, paper, scissor. R is rock, P is paper and S is scissor
import random

List = ['R', 'P', 'S']

attempt = 3
player_attempt = 0
win_count = 0
lose_count = 0
won_plural = ""
lost_plural = ""


while player_attempt < attempt:
    player_choice = input("choose R(rock),P(paper),S(scissor)= ")
    com_choice = random.choice(List)
    win_conditions = player_choice.upper() == "P" and com_choice == "R" or player_choice.upper() == "R" and com_choice\
    == "S" or player_choice.upper() == "S" and com_choice == "P"
    lose_conditions = com_choice == "P" and player_choice.upper() == "R" or com_choice == "R" and player_choice.upper()\
                                    == "S" or com_choice == "S" and player_choice.upper() == "P"
    draw_conditions = player_choice.upper() == "R" and com_choice == "R" or player_choice.upper() == "P" and com_choice\
                                    == "P" or player_choice.upper() == "S" and com_choice == "S"
    if lose_conditions:
        print(f"computer's choice is {com_choice}, you chose {player_choice.upper()}")
        print("you lose")
        player_attempt += 1
        lose_count += 1
    if win_conditions:
        print(f"computer's choice is {com_choice}, you chose {player_choice.upper()}")
        print("you win")
        player_attempt += 1
        win_count += 1
    if draw_conditions:
        print(f"computer's choice is {com_choice}, you chose {player_choice.upper()}")
        print("try again")
else:
    if win_count > 1:
        won_plural = "s"
    if lose_count > 1:
        lost_plural = "s"
    print(f"game over, you won {win_count} time{won_plural} and you lost {lose_count} time{lost_plural}")
