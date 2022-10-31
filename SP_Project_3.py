
def load_puzzle( path ):
    with open(path) as path:  
        contents = path.read()
        lines = contents.split('\n')   
    puzzle = []
    for i in range(0,len(lines)):
        token_ints = []
        token_strings = lines[i].split(' ')
        for x in range(0,len(token_strings)):
            token_ints.append(int(token_strings[x]))
        puzzle.append(token_ints)
    return puzzle
 
def display_puzzle( puzzle ):
    print('+-------+-------+-------+')
    for r in range(0, len(puzzle)):
        row = '| '
        for col in range (0,len(puzzle[r])):
            if(puzzle[r][col] == 0):
                row = row + '. '
            else:
                row = row + str( puzzle[r][col] ) + ' '
            if (col == 2) or  (col == 5) or (col == 8):
                row = row + '| '
        print(row)
        if (r == 2) or  (r == 5) or (r == 8):
            print('+-------+-------+-------+')
            
def get_next( row, col ):
    if col < 8:
        return( row and col + 1 )
    if col == 8 and row < 8:
        return( row + 1 and 0 )
    if col == 8 and row == 8:
        return(None and None)
    
def copy_puzzle( puzzle ):
    new_puzzle = []
    for i in range (0, len(puzzle)):
        new_puzzle = new_puzzle + puzzle[i].copy()
    return new_puzzle

def get_options(puzzle, row, col):
    if (puzzle[row][col] > 0):
        return None
    used = []
    # check the row
    for c in range(0, len(puzzle)):
        if (puzzle[row][c]> 0):
            used.append(puzzle[row][c])
    # check the column
    for r in range(0, len(puzzle)):
        if (puzzle[r][col]> 0):
            used.append(puzzle[r][col])
    
    # check the block
    start_row = 3*int(row/3)
    start_col = 3*int(col/3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col,start_col +  3):
            if (puzzle[r][c]> 0):
                used.append(puzzle[r][c])
    
    # find valid options
    options = []
    isUsed  = [False,False,False,False,False,False,False,False,False,False]
    for i in used:
        isUsed[i] = True
    for i in range(1,len(isUsed)):
        if isUsed[i] == False:
          options.append(i)

    return options


#def IsPuzzleSovled(puzzle):
#   for r in range(0,10):
#        for c in range(0,10):
#            if (puzzle[r][c] == 0):
#                return False
#    return True
#
#def solve(puzzle):
#   while IsPuzzleSovled(puzzle) == False:
#        for r in range(0,9):
#            for c in range(0,9):
#                if (puzzle[r][c] == 0):
#                    options = get_options(puzzle, r, c)
#                    if len(options) == 1:
#                        puzzle[r][c] = options[0];

def solve(puzzle, row = 0, col = 0):
    next_row, next_col = get_next(row, col)
    if next_row == None:
         return puzzle
    if next_row != None:
        solve(puzzle, next_row, next_col)
    for r in range(0,10):
        options = get_options(puzzle, row, col)
        if len(options) == 0:
            return None
        else:
            new_puzzle = copy_puzzle(puzzle)
            new_puzzle = new_puzzle[row][col]
            
    result = solve(new_puzzle, row, col)
    if result != None:
        return result
    else:
        return None
            

#puzzle = load_puzzle("puzzle01.txt")
puzzle = load_puzzle("puzzleTest.txt")
#print(get_options(puzzle, 2, 4))
#print(get_options(puzzle, 2, 5))

puzzle = solve(puzzle)

display_puzzle(puzzle)

