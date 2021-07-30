'''solver sudoku'''
import time

board = [
    [0,0,1,0,0,7,0,0,0],
    [5,0,9,8,0,0,0,0,0],
    [0,6,4,0,1,5,0,0,8],
    [4,0,0,0,0,0,5,0,0],
    [0,0,7,0,3,1,9,0,0],
    [0,0,8,2,0,0,0,0,6],
    [0,0,0,0,0,0,2,0,0],
    [6,1,0,0,9,2,0,0,0],
    [0,0,2,1,0,0,0,5,0]
]



def empty_box():
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j]==0:
                return [i,j]
    return False

def valid_box(board, position, number):

    #row
    for i in range (len(board)):
        if board[position[0]][i] == number and i!= position[1]:
            return False

    #column
    for j in range (len(board[0])):
        if board[j][position[1]] == number and j != position[0]:
            return False

    #boxof9
    for i in range ((position[0]//3)*3,((position[0]//3)*3)+3):
        for j in range((position[1]//3)*3,((position[1]//3)*3)+3):
            if board[i][j] == number and [i,j] != position:
                return False
    return True



def solver_sudoku(board,i,j):
    if empty_box():
        i,j = empty_box()
    else:return True
    for k in range (1,10):
        if valid_box(board,[i,j], k):
            board[i][j] = k

            if solver_sudoku(board,i,j):
                return True

            else:
                 board[i][j] = 0
    return False

ti=time.time()
solver_sudoku(board,i,j)
tf=time.time()
for k in range (len(board)):
    print(*board[k])
print((tf-ti)*10**3)

