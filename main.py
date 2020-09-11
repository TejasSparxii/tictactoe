grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

points = {'human' : -1 , 'AI' : 1 , 'Tie' : 0}

def win(grid):
    # horizontal winner

    for col, row in enumerate(grid):
        if row.count(row[0]) == len(grid) and row[0] == 1:
            return 'human'
        elif row.count(row[0]) == len(grid) and row[0] ==2:
            return 'AI'
    # vertical winner
    gp3 = []

    for i in range(len(grid)):
        for row in grid:
            gp3.append(row[i])
        if gp3.count(gp3[0]) == len(grid) and gp3[0] == 1:
            return 'human'
        elif gp3.count(gp3[0]) == len(grid) and gp3[0] == 2:
            return 'AI'

        gp3 = []

    # diagonal winner

    # \ type of digonal
    grp1 = []

    for i, row in enumerate(grid):
        grp1.append(row[i])
    if grp1.count(grp1[0]) == len(grid) and grp1[0] == 1:
        return 'human'
    elif grp1.count(grp1[0]) == len(grid) and grp1[0] == 2:
        return 'AI'
    # / type of diagonal
    grp2 = []

    n = list(range(len(grid)))
    m = list(reversed(range(len(grid))))

    for ind, row in zip(n, m):
        grp2.append(grid[ind][row])

    if grp2.count(grp2[0]) == len(grid) and grp2[0] == 1:
        return 'human'
    elif grp2.count(grp2[0]) == len(grid) and grp2[0] == 2:
        return 'AI'

    #tie check

    tie = []
    for rows in grid:
        tie = tie + rows
    if tie.count(0) == 0:
        return 'Tie'



def minimax(grid, player):
    result = win(grid)
    if result != None:
        score = points[result]
        return score

    if (player == 'AI'):
        BestScore = -10
        for rnum, rows in enumerate(grid):
            for cnum, cols in enumerate(rows):
                if grid[rnum][cnum] == 0:
                    grid[rnum][cnum] = 2
                    score = minimax(grid, 'Human')
                    grid[rnum][cnum] = 0

                    BestScore = max(score, BestScore)
        return BestScore

    else:
        BestScore = 10
        for rnum, rows in enumerate(grid):
            for cnum, cols in enumerate(rows):
                if grid[rnum][cnum] == 0:
                    grid[rnum][cnum] = 1
                    score = minimax(grid, 'AI')
                    grid[rnum][cnum] = 0

                    BestScore = min(score, BestScore)
        return BestScore



def main(grid):
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    print(grid[0][0], '|', grid[0][1], '|', grid[0][2], '         1  2  3')
    print(grid[1][0], '|', grid[1][1], '|', grid[1][2], ' <<==>>  4  5  6')
    print(grid[2][0], '|', grid[2][1], '|', grid[2][2], '         7  8  9')

    points = {'Human': -1, 'AI': 1, 'Tie': 0}

    while True:
        PlayerMove = int(input('Enter your move : '))
        if PlayerMove < 1 or PlayerMove > 9:
            print('Enter a Valid Move')
            continue

        PlayerMove = PlayerMove - 1
        row = PlayerMove // 3
        column = (PlayerMove % 3)

        if grid[row][column] != 0:
            print('Place is occupied, select different move')
            continue

        grid[row][column] = 1

        result = win(grid)
        if result != None:
            if result == 'Tie':
                print('Match Tied!!!!')
            else:
                print(result, 'won')
            break

        BestScore = -10
        BestMove = []
        for rnum, rows in enumerate(grid):
            for cnum, cols in enumerate(rows):
                if grid[rnum][cnum] == 0:
                    grid[rnum][cnum] = 2
                    score = minimax(grid, 'human')
                    grid[rnum][cnum] = 0

                    if score > BestScore:
                        BestScore = score
                        BestMove = [rnum, cnum]

        grid[BestMove[0]][BestMove[1]] = 2

        print(grid[0][0], '|', grid[0][1], '|', grid[0][2], '       1  2  3')
        print(grid[1][0], '|', grid[1][1], '|', grid[1][2], ' <==>  4  5  6')
        print(grid[2][0], '|', grid[2][1], '|', grid[2][2], '       7  8  9')

        result = win(grid)
        if result != None:
            if result == 'Tie':
                print('Tie match')
            else:
                print(result, 'won')
            break



main(grid)
