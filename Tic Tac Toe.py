# board to display as a List
board_list = ['','1','2','3','4','5','6','7','8','9']

# To board on as new board
def clear_output():
    print("\n"*20)


# To display the board
def display(board):
    clear_output()
    print(board[1] , '|', board[2] , '|' , board[3])
    print(board[4] , '|', board[5] , '|' , board[6])
    print(board[7] , '|', board[8] , '|' , board[9])


#To set X and O at required position as per user input
def change_list(x,flag):
    if flag:
        board_list[x] = 'X'
    else:
        board_list[x] = 'O'


# To Check the Winner
def check_winner(board):
    if board[1] == board[2] == board[3]:
        return True
    if board[4] == board[5] == board[6]:
        return True
    if board[6] == board[8] == board[9]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[3] == board[6] == board[9]:
        return True
    if board[1] == board[5] == board[9]:
        return True
    if board[3] == board[5] == board[7]:
        return True
    else:
        return False


# To take input from user               
def user_input():
    ch = []                 # List to store the position user has already entered
    marker = ''             # Get player X or O mard
    while marker != 'X' and marker != 'x' and marker != 'o' and marker != 'O':
        marker  = input ("Player 1 choose X or O: ")
    
    if marker == 'x' or marker == 'X':  # Flag to store X or O as per user
        flag  = True                
    else:
        flag = False
    i = 1
    display(board_list)     # To display the board First time
    while i <= 9:           # While loop  
        if i%2 == 0
        :        
            print ("Player 2 chance to select")
        else:
            print ("Player 1 chance to select")
        x = int(input("Enter number position to mark:  "))  # postion to mark by user
        if x not in ch:                 # Condition to check if user is entering the already selected position
            change_list(x,flag)         # Change the Board_list list and flag to set X or O
            flag = not flag             # Switching the mark
            i += 1                      
            ch.append(x)                # Store entered position in ch list to check later
            display(board_list)
            if check_winner(board_list):                    # Check winner
                if i%2 == 0:
                    print("Player 1 won")
                else:
                    print("Player 2 won")
                play_game()
                        
        else:                           # if user enter same position twice
            print("already Entered number")
    else:                               # While else function if no one win's
        
        print("No one win")
        play_game()


        
def play_game():                        # Function to start game

    global board_list                   # If user want to play again we reset the board_list List with predefined values
    board_list = ['','1','2','3','4','5','6','7','8','9']
    x = int(input("Press 1 to play game and other key to exit"))    # Check if user want to continue
    if x == 1:
        user_input()                    # If user want to continue we start the game
    else:
        exit()                          # if user don't want to continue


play_game()                             # Calling the play_game  function

