#----------Global variables-------

#Game board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
#if the game is still going
game_is_still_on=True

#who won? Or tie?
winner=None

#who's turn is it
current_player="X"
c=True



def display_boards():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def Play_game():
    global c
    #display initial board
    display_boards()
    while game_is_still_on:
        handle_turn(current_player)

        check_if_game_over()
        if c==True:
            flip_player()
     #game ended
    if winner=="X" or winner=="O":
        print(winner+"won")
    elif winner==None:
        print("tie")

    
def handle_turn(player):
    global c
    print(player + "'s turn.")
    position=input("choose a position from 1-9:")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("invalid input.Choose a position from 1-9: ")
        else:
            break


    position=int(position)-1
    if board[position]== "-":
        valid = True
        board[position]=player
        c=True
    else:
      print("You can't go there. Go again.")
      c=False

    
    display_boards()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    #check rows
    row=check_rows()
    #check coloumns
    coloumn=check_coloumns()
    #check diagonals
    diagonal=Check_diagonals()
    if row:
        winner=row
    elif coloumn:
        winner=coloumn
    elif diagonal:
        winner=diagonal
    else:
        winner=None
    return
def check_rows():
    global game_is_still_on
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[4]==board[5]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    if row1 or row2 or row3:
        game_is_still_on=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return
def check_coloumns():
    global game_is_still_on
    coloumn1=board[0]==board[3]==board[6]!="-"
    coloumn2=board[1]==board[4]==board[7]!="-"
    coloumn3=board[2]==board[5]==board[8]!="-"
    if coloumn1 or coloumn2 or coloumn3:
        game_is_still_on=False
    if coloumn1:
        return board[0]
    elif coloumn2:
        return board[1]
    elif coloumn3:
        return board[2]
    return

def Check_diagonals():
    global game_is_still_on
    diagonal1=board[0]==board[4]==board[8]!="-"
    diagonal2=board[2]==board[4]==board[6]!="-"
    
    if diagonal1 or diagonal2:
        game_is_still_on=False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return
    
def check_if_tie():
    global game_is_still_on
    if "-" not in board:
        game_is_still_on=False
    return

def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    
    return
    
    
Play_game()
    















#board
#display board
#play game
#check win
  #check rows
  #check coloumns
  #check diagonals
#check tie
#flip Player
