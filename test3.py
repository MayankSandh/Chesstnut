def isKingUnderCheck(board, currentTurn):
    row, col = 0,0
    for r in range(8):
        for c in range(8):
           if board[r][c] // 7 == currentTurn and board[row][col]% 7 == 1:
               row, col = r,c
    if currentTurn:
        mult = -1
    else:
        mult = 1
    legal_moves = list()

    directions = ((1,1), (1,-1), (-1,1), (-1,-1)) # bishop pawn queen checker
    for d in directions:
        pos = [row, col]
        while isValid(board, pos, legal_moves, row, col, currentTurn):
            legal_moves.append(pos)
            pos = list((map(add, pos, d)))
        if board[row][col]//7 == (not currentTurn) and (board[row][col]%7 == 6 or board[row][col]%7 == 5 or board[row][col]%7 == 2):
            return True
                
    directions = ((0,1), (0,-1), (-1,0), (1,0)) # rook queen checker
    for d in directions:
        pos = [row, col]
        while isValid(board, pos, legal_moves, row, col, currentTurn):
            legal_moves.append(pos)
            pos = list((map(add, pos, d)))
        if board[row][col]//7 == (not currentTurn) and (board[row][col]%7 == 3 or board[row][col]%7 == 2):
            return True

    direction = ((2,1), (2,-1), (-1,2), (1,2),(-2,1), (-2,-1), (-1,-2), (1,-2)) # knight checker
    for x,y in direction:
        if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
            if isValid(board, [row+x, col+y], legal_moves, row, col, currentTurn):
                legal_moves.append([row+x, col+y])
            if board[row+x][col+y]//7 == (not currentTurn) and (board[row+x][col+y]%7 == 4):
                return True

    return False