def check_sos(board, row, col, letter):
    global first_player_score
    global second_player_score
    global counter_play
    
    if letter == "s":
        if (board[row + 1][col + 1] == board[row + 1][col + 3] == "s" and board[row + 1][col + 2] == "o") or \
           (board[row + 1][col + 1] == board[row + 1][col - 1] == "s" and board[row + 1][col] == "o") or \
           (board[row + 1][col + 1] == board[row + 3][col + 1] == "s" and board[row + 2][col + 1] == "o") or \
           (board[row + 1][col + 1] == board[row - 1][col + 1] == "s" and board[row][col + 1] == "o") or \
           (board[row + 1][col + 1] == board[row + 3][col + 3] == "s" and board[row + 2][col + 2] == "o") or \
           (board[row + 1][col + 1] == board[row - 1][col - 1] == "s" and board[row][col] == "o"):
            if counter_play % 2 == 0:  # Check if it's the first player's turn
                first_player_score += 1
                counter_play += 1
                return True
            else:
                second_player_score += 1
                counter_play += 1
                return True
    elif letter == "o":
        if (board[row + 1][col] == board[row + 1][col + 2] == "s" and board[row + 1][col + 1] == "o") or \
           (board[row][col + 1] == board[row + 2][col + 1] == "s" and board[row + 1][col + 1] == "o") or \
           (board[row][col] == board[row + 2][col + 2] == "s" and board[row + 1][col + 1] == "o") or \
           (board[row][col + 2] == board[row + 2][col] == "s" and board[row + 1][col + 1] == "o"):
            if counter_play % 2 == 0:  # Check if it's the first player's turn
                first_player_score += 1
                counter_play += 1
                return True
            else:
                second_player_score += 1
                counter_play += 1
                return True
    else:
        pass

def player_input(player_number):
    global counter_play
    global counter_board
    
    input_letter = input(f"{player_number} player please enter your letter s or o: ")
    row = int(input(f"{player_number} player please enter position row from 1-4: ")) - 1
    col = int(input(f"{player_number} player please enter position column from 1-4: ")) - 1
    
    counter_board += 1
    board[row + 1][col + 1] = input_letter
    
    if check_sos(board, row, col, input_letter):
        if counter_play % 2 == 0:  # Check if it's the first player's turn
            player_input("1")
        else:
            player_input("2")
    else:
        counter_play += 1

def print_board(board):
    print("| " + board[2][2] + " | " + board[2][3] + " | " + board[2][4] + " | " + board[2][5] + " | ")
    print("---------------------")
    print("| " + board[3][2] + " | " + board[3][3] + " | " + board[3][4] + " | " + board[3][5] + " | ")
    print("---------------------")
    print("| " + board[4][2] + " | " + board[4][3] + " | " + board[4][4] + " | " + board[4][5] + " | ")
    print("---------------------")
    print("| " + board[5][2] + " | " + board[5][3] + " | " + board[5][4] + " | " + board[5][5] + " | ")

def check_win():
    global first_player_score
    global second_player_score
    if second_player_score > first_player_score:
        print("The winner is the second player.")
        print("Second player score:", second_player_score)
        print("First player score:", first_player_score)
    elif first_player_score > second_player_score:
        print("The winner is the first player.")
        print("First player score:", first_player_score)
        print("Second player score:", second_player_score)
    else:
        print("It is a tie game.")
        print("First player score:", first_player_score)
        print("Second player score:", second_player_score)

def board_fill():
    global running_game
    if counter_board == 16:
        running_game = False
        check_win()

def play_game():
    global running_game
    while running_game:
        player_input("1")
        print_board(board)
        board_fill()
        if running_game:
            player_input("2")
            print_board(board)
            board_fill()

board = [["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]]

first_player_score = 0
second_player_score = 0
running_game = True
counter_board = 0
counter_play = 0

print("WELCOME TO SOS GAME")
play_game()
