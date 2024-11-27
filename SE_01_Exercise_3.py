import random

print("Welcome to A Master Mind")
print("------------------------")

gameBoard = [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],['X', 'X', 'X', 'X'],]
rows = 12
cols = 4

#BoardSize

def Board():
    for x in range(rows):
        print("+---+---+---+---+") 
        print("|", end="")
        for y in range(cols):
            print("",gameBoard[x][y], end=" |")
        print("\n+---+---+---+---+")

turn = 0

#BoardPannels

def Array(input_count, color_sel):
    
    if (turn == 0):
        gameBoard[0][input_count] = color_sel
    elif (turn == 1):
        gameBoard[1][input_count] = color_sel
    elif (turn == 2):
        gameBoard[2][input_count] = color_sel
    elif (turn == 3):
        gameBoard[3][input_count] = color_sel
    elif (turn == 4):
        gameBoard[4][input_count] = color_sel
    elif (turn == 5):
        gameBoard[5][input_count] = color_sel
    elif (turn == 6):
        gameBoard[6][input_count] = color_sel
    elif (turn == 7):
        gameBoard[7][input_count] = color_sel
    elif (turn == 8):
        gameBoard[8][input_count] = color_sel
    elif (turn == 9):
        gameBoard[9][input_count] = color_sel
    elif (turn == 10):
        gameBoard[10][input_count] = color_sel
    elif (turn == 11):
        gameBoard[11][input_count] = color_sel

#Player code selection

player_input = int(input("\n Choose a color combination:"))
code = [int(digit) for digit in str(player_input)]
fail = []


while turn <= 12:
    hint_cor = 0
    hint_in = 0
    rowIn = 0
    input_count = 0

    if turn == 0: #Creates initial code
        for times in range(4): 
            color_sel = random.randint(1,6)
            if color_sel >= 1 and color_sel <= 6:
                Array(input_count, color_sel)
                input_count += 1
    elif hint_in >= 1 and hint_cor == 0: #Checks if numbers were present
        gameBoard[turn] = random.shuffle(gameBoard[turn - 1]) 
            if gameBoard[turn]  #This is where i finished coding <----------- I was making sure to add a list of failed attempts so if it ever generates the attempt agains it would be re made.
        fail.append(gameBoard[turn - 1])

    else:  #If no sucesss generates new code
        for times in range(4):
            color_sel = random.randint(1,6)
            if color_sel >= 1 and color_sel <= 6:
                Array(input_count, color_sel)
                input_count += 1
            
    Board()

    #Feedback loop

    for i in range(4):
        if gameBoard[turn][rowIn] == code[rowIn]:
            code[rowIn] = 0
            hint_cor += 1
        rowIn += 1

    rowIn = 0
    for b in range(4):
        if gameBoard[turn][rowIn] in code:
            hint_in += 1
        rowIn += 1

    print(hint_cor)
    print(hint_in)
    turn += 1


# while turn != 13:
#     Board()
#     anwser = [4, 5, 2, 1]
#     input_count = 0
#     for times in range(4):
#         color_sel = int(input("\n Choose a color: "))
#         if color_sel >= 1 and color_sel <= 6:
#             Array(input_count, color_sel)
#             input_count += 1

#     if input_count == 4:
#         input_count = 0

#     hint_cor = 0
#     hint_in = 0
#     rowIn = 0

#     for i in range(4):
#         if gameBoard[turn][rowIn] == anwser[rowIn]:
#             anwser[rowIn] = 0
#             hint_cor += 1

#         rowIn += 1
    
#     rowIn = 0
#     for b in range(4):
#         if gameBoard[turn][rowIn] in anwser:
#             hint_in += 1

#         rowIn += 1

#     if hint_cor == 4:
#         print('\nYou guessed all pins correctly, You Win!')
#     elif hint_cor >= 1 and hint_cor < 4 and hint_in == 0:
#         print('\nHint: You guessed ' + str(hint_cor) + ' pins correctly!')
#     elif hint_cor == 0 and hint_in >= 1:
#         print('\nHint: You guessed ' + str(hint_in) + ' but not in the right position.')
#     elif hint_cor >= 1 and hint_cor < 4 and hint_in >= 1:
#         print('\nHint: You guessed ' + str(hint_cor) + ' pins correctly, and ' + str(hint_in) + ' pins that are not in the correct position.' )

#     turn += 1