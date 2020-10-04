board = [
    [4,0,0,0,0,6,8,0,0],
    [2,0,0,8,0,0,0,0,9],
    [9,0,1,0,0,3,0,5,6],
    [0,0,9,6,8,0,0,0,2],
    [0,1,0,0,0,0,5,9,0],
    [0,0,8,0,0,9,7,0,0],
    [0,2,4,0,9,0,0,0,0],
    [1,0,0,0,0,0,4,0,0],
    [0,0,7,3,0,0,0,0,0]
]

def print_board(bo):
    """ Print the boad correctly"""

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo)):
            if j % 3 == 0 and j !=0:
                print(" | ", end="")

            if j==8:
                print(str(bo[i][j]))
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    ''' Find the empty square '''

    for i in range(len(bo)):
       for j in range(len(bo)): 
           if bo[i][j] == 0:
               return (i, j) # row, column
    return None

def valid(bo, num, pos):
    ''' Check if the suggested number is valid '''
    
    #Check row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False
    #Check column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and j != pos[0]:
            return False
    #Check box
    box_y = pos[1]//3
    box_x = pos[0]//3

    for i in range(box_x*3,box_x*3+3):
      for j in range(box_y*3,box_y*3+3):
          if bo[i][j]==num and (i, j)!= pos:
              return False
    return True

def solver(bo):
    ''' Solve the Sudoku '''
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for n in range(1,10):
        if valid(bo, n , (row, col)):
            bo[row][col] = n
            if solver(bo):
                return True
            bo[row][col] = 0
    return False

solver(board)
print("___________________")
print_board(board)

