# number guessing (1 to 100)
# please delete the line 9 when this is finalised
import random

number_range = range(1, 100)
number_list = list(number_range)
correct_answer = (random.choice(number_list))

print(correct_answer)
# here I put the word "range" because i not sure what word to use
chances_to_guess_the_right_range = 4
chances_to_guess_the_right_number = 3
attempt_to_guess_number_range = 0
attempt_to_guess_answer = 0

while attempt_to_guess_number_range < chances_to_guess_the_right_range:
    guess1 = input('guess a range of number from (only numerical number)= ')
    guess2 = input('until (only numerical number)= ')
    if int(guess1) == correct_answer or int(guess2) == correct_answer:
        print(f"lucky you, either {guess1} or {guess2} is the right answer")
        lucky_attempt = input(f"pick one now (either {guess1} or {guess2})= ")
        if int(lucky_attempt) == correct_answer:
            print(f"you are correct, right answer is {correct_answer}")
            break
        elif int(lucky_attempt) != correct_answer:
            print(f"game over, right answer is {correct_answer}")
            break

    given_answer = range(int(guess1), int(guess2))
    given_list = list(given_answer)

    if correct_answer in given_list:
        attempt_to_guess_number_range += 1
        remaining_attempt = chances_to_guess_the_right_range - attempt_to_guess_number_range
        print(" you are within the correct range")
        print(f" you have {remaining_attempt} left to guess the range")
        print(f" this is the current range of your answer: from {guess1} to {guess2}")
    if correct_answer not in given_list:
        attempt_to_guess_number_range += 1
        remaining_attempt = chances_to_guess_the_right_range - attempt_to_guess_number_range
        print(" you are not within the correct range")
        print(f" you have {remaining_attempt} chances left to guess the range")

else:
    print(f"this is your current range of answer, from {guess1} to {guess2} ")
    print(" now you have another 3 chances to guess the right answer")
    while attempt_to_guess_answer < chances_to_guess_the_right_number:
        guess_the_answer = input("choose your answer (in number)= ")
        attempt_to_guess_answer += 1
        if int(guess_the_answer) == correct_answer:
            print(f"you are correct, right answer is {correct_answer}")
            break
        if guess_the_answer != correct_answer:
            remaining_attempt = chances_to_guess_the_right_number-attempt_to_guess_answer
            print(f"you have {remaining_attempt} chances left to guess")
            if int(guess_the_answer) < correct_answer:
                print("your answer should be higher")
            if int(guess_the_answer) > correct_answer:
                print("your answer should be lower")
    else:
        print("game over")
        print(f"right answer is {correct_answer}")

# the weaknesses in this is that you can only put number as an answer. if you put non number, the software will crash
# on line 37 there is an issue of unidentified name, don't know how to solve
