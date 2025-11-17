board = [["1" for _ in range(3)] for _ in range(3)]
for row in range(3):
    ROW  = list(map(int,input().split()))
    for col in range(3):
        action = int(ROW[col])
        
        if action % 2:
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for dr,dc in directions:
                r = row+dr
                c = col+dc
                if  (0<=r<3 and 0<=c<3):
                    board[r][c] = "0"if board[r][c] == "1" else "1"
                    
            board[row][col] = "0" if board[row][col] == "1" else "1"
                    
for Row in board:
    print("".join(Row))
                
    
    
    