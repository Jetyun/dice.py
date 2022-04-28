

game_plan0 = ["1", "2", "3"]
game_plan1 = ["4", "5", "6"]
game_plan2 = ["7", "8", "9"]

# in programming with Mosh, they teach you about using {} to link the parameter, but in this case, if you use {}. it will come out an error Unexpected type(s):(set)Possible type(s):(SupportsIndex)(slice)

def player1():
    instruction = int(input('instruction for P1: '))
    if instruction == 1:
        game_plan0[0] = 'x'
    elif instruction == 2:
        game_plan0[1] = 'x'
    elif instruction == 3:
        game_plan0[2] = 'x'
    elif instruction == 4:
        game_plan1[0] = 'x'
    elif instruction == 5:
        game_plan1[1] = 'x'
    elif instruction == 6:
        game_plan1[2] = 'x'
    elif instruction == 7:
        game_plan2[0] = 'x'
    elif instruction == 8:
        game_plan2[1] = 'x'
    elif instruction == 9:
        game_plan2[2] = 'x'


def player2():
    instruction2 = int(input('instruction for P2: '))
    if instruction2 == 1:
        game_plan0[0] = 'y'
    elif instruction2 == 2:
        game_plan0[1] = 'y'
    elif instruction2 == 3:
        game_plan0[2] = 'y'
    elif instruction2 == 4:
        game_plan1[0] = 'y'
    elif instruction2 == 5:
        game_plan1[1] = 'y'
    elif instruction2 == 6:
        game_plan1[2] = 'y'
    elif instruction2 == 7:
        game_plan2[0] = 'y'
    elif instruction2 == 8:
        game_plan2[1] = 'y'
    elif instruction2 == 9:
        game_plan2[2] = 'y'

def revert():


print(game_plan0)
print(game_plan1)
print(game_plan2)


while game_plan0[0-2] != 'x' or game_plan1[0-2] != 'x' or game_plan2[0-2] != 'x' or game_plan0[0-2] != 'y' or game_plan1[0-2] != 'y' or game_plan2[0-2] != 'y' or game_plan0[0] and game_plan1[0] and game_plan2[0] != 'x' or game_plan0[1] and game_plan1[1] and game_plan2[1] != 'x' or game_plan0[2] and game_plan1[2] and game_plan2[2] != 'x' or game_plan0[0] and game_plan1[0] and game_plan2[0] != 'y' or game_plan0[1] and game_plan1[1] and game_plan2[1] != 'y' or game_plan0[2] and game_plan1[2] and game_plan2[2] != 'y' or game_plan0[0] and game_plan1[1] and game_plan2[2] != 'x' or game_plan0[0] and game_plan1[1] and game_plan2[2] != 'y' or game_plan0[2] and game_plan1[1] and game_plan2[0] != 'x' or game_plan0[2] and game_plan1[1] and game_plan2[0] != 'y':
    player1()
    print(game_plan0)
    print(game_plan1)
    print(game_plan2)
    player2()
    print(game_plan0)
    print(game_plan1)
    print(game_plan2)
    if game_plan0[0] == 'x' or game_plan0[1] == 'x' or game_plan0[2] == 'x' or game_plan1[0] == 'x' or game_plan1[1] == 'x' or game_plan1[2] == 'x' or game_plan2[0] == 'x' or game_plan2[1] == 'x' or game_plan2[2] == 'x':
        print('space not available')
    elif game_plan0[0] == 'y' or game_plan0[1] == 'y' or game_plan0[2] == 'y' or game_plan1[0] == 'y' or game_plan1[1] == 'y' or game_plan1[2] == 'y' or game_plan2[0] == 'y' or game_plan2[1] == 'y' or game_plan2[2] == 'y':
        print('space not available')
else:
    if game_plan0[0-2] == 'x' or game_plan1[0-2] == 'x' or game_plan2[0-2] == 'x' or game_plan0[0-2] == 'x' or game_plan1[0-2] == 'x' or game_plan2[0-2] == 'x' or game_plan0[0] and game_plan1[0] and game_plan1[0] == 'x' or game_plan0[1] and game_plan1[1] and game_plan2[1] == 'x' or game_plan0[2] and game_plan1[2] and game_plan2[2] == 'x' or game_plan0[0] and game_plan1[1] and game_plan2[2] == 'x' or game_plan0[2] and game_plan1[1] and game_plan2[0] == 'x':
        print("player 1 wins")

    elif game_plan0[0-2] == 'y' or game_plan1[0-2] == 'y' or game_plan2[0-2] == 'y' or game_plan0[0-2] == 'y' or game_plan1[0-2] == 'y' or game_plan2[0-2] == 'y' or game_plan0[0] and game_plan1[0] and game_plan1[0] == 'y' or game_plan0[1] and game_plan1[1] and game_plan2[1] == 'y' or game_plan0[2] and game_plan1[2] and game_plan2[2] == 'y' or game_plan0[0] and game_plan1[1] and game_plan2[2] == 'y' or game_plan0[2] and game_plan1[1] and game_plan2[0] == 'y':
        print("player 2 wins")

