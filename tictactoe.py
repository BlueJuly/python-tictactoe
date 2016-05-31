# Prints the board in a pretty format.
# Input: Board.
# Output: None.
def printBoard(b):
    for r in range(3):
        print "[", b[r][0], b[r][1], b[r][2], "]"

# Returns the other player.
# Input: Player "O" or "X".
# Output: Other player.
def otherPlayer(p):
    if p == "O":
        return "X"
    else:
        return "O"

# Detects whether a given player has won the game.
# Input: Board. Player "O" or "X".
# Output: Boolean.
def hasWon(b, p):
        if b[0][0]==b[0][1] == b[0][2]==p or b[1][0]==b[1][1] == b[1][2]==p or b[2][0]==b[2][1] == b[2][2]==p:
            return True
        if b[0][0]==b[1][0] == b[2][0]==p or b[0][1]==b[1][1] == b[2][1]==p or b[0][2]==b[1][2] == b[2][2]==p:
            return True
        return (b[0][0]==b[1][1]==b[2][2]==p or b[0][2]==b[1][1] ==b[2][0]==p)

# Selects the next move for the given player.
# Input: Board. Player "O" or "X".
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def move(b, p, flag):
    # nextplayer = "X" if p=="O" else "O"
    if hasWon(b,p if flag else otherPlayer(p)) :
        return 1,[-1,-1]
    if hasWon(b, otherPlayer(p) if flag else p):
        return -1,[-1,-1]
    res_list=[] # list for appending the resultn 
    c = max([r.count(' ') for r in b])
    # print 'c:',c
    if  c is 0:
        return 0,[0,-1]
    _list=[] # list for storing the indexes where '-' appears
    for i in range(len(b)):
        for j in range (len(b[i])):
         if b[i][j] == ' ':
            _list.append([i,j])
    #tempboardlist=list(board)
    for i in _list:
        b[i[0]][i[1]]=p
        ret,_move=move(b,otherPlayer(p), not flag)
        res_list.append(ret)
        b[i[0]][i[1]]=' '

    if flag:
        maxele=max(res_list)
        return maxele,_list[res_list.index(maxele)]
    else :
        minele=min(res_list)
        return minele,_list[res_list.index(minele)]

# Plays the computer against itself.
# Input: None.
# Output: None.
def computerVsComputer():
    # Initialize the game.
    board = [[" ", " " ," "], [" ", " " ," "], [" ", " " ," "]]
    player = "X"
    turns = 0
    printBoard(board)
    # Run the game.
    while turns < 9 and not hasWon(board, "X") and not hasWon(board, "O"):
        s, m = move(board, player, True)
        if m == None or board[m[0]][m[1]] != " ":
            print "Invalid move", m, "by player", player, "on this board:"
            printBoard(board)
            return
        board[m[0]][m[1]] = player
        print
        printBoard(board)
        player = otherPlayer(player)
        turns = turns + 1
    # Finish the game.
    if hasWon(board, "O"):
        print "O wins."
    elif hasWon(board, "X"):
        print "X wins."
    else:
        print "Draw."

# If the user ran this file directly, then this code will be executed.
# If the user imported this file, then this code will not be executed.
if __name__ == "__main__":
      computerVsComputer()
  