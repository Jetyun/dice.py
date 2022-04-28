# Hangman

question_not_lowered = input("what's your choice of word in Hangman= ")
question = question_not_lowered.lower()


print(f' the word you must guess contained {len(question)} characters')
question_bar = ""
question_bar += "_"*len(question)
listed_question_bar = list(question_bar)
print(listed_question_bar)

listed_question = list(question)
# reason for line 12 is because the "and" operator doesn't work if i put '....and "_" in listed question bar"
# reason for line 24,36,39,40 is because they used to break out of while loop (the line 38 only breaks for loop)
blank_space = "_"


attempt = 0
chances = len(question)+2
print(f"you may attempt to guess for {chances} times")
plural = ''
if chances > 2:
    plural += "s"
while attempt < chances:
    break_flag = False
    Input = input("please input one alphabet you think it is correct= ")
    input_answer = Input.lower()
    attempt += 1
    remaining_chances = chances-attempt
    if input_answer in listed_question and blank_space in listed_question_bar:
        print(f"you have {remaining_chances} chance{plural} left")
        for ans in range(len(listed_question)):
            if listed_question[ans] == input_answer:
                listed_question_bar.pop(ans)
                listed_question_bar.insert(ans, input_answer)
                if "_" not in listed_question_bar:
                    break_flag = True
                    print("you win, game over")
                    break
        if break_flag:
            break
        print(listed_question_bar)
    elif input_answer not in listed_question:
        print("you guessed incorrectly, or you are not inserting ONE ALPHABET, try again")
        print(f"you have {remaining_chances} chance{plural} left")

else:
    print("game over, no more attempt left")
