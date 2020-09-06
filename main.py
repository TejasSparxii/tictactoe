import itertools
box=[[0, 0, 0 ],
     [0, 0, 0 ],
     [0, 0, 0 ]]
def winner(board):

    print("0, 1, 2")
    #horrizontal winner
    for col,row in enumerate(box):
        print(row,col)
        if row.count(row[0])==len(box) and row[0]!=0:
            print(f"the winner is player {row[0]} by horizontal matching")
            return (1)
    #vertical winner
    gp1=[]
    for i in range(3):
        for row in box:
            gp1.append(row[i])
        if gp1.count(gp1[0]) == len(box) and gp1[0] != 0:
            print(f"{gp1[0]} is winner vertically")
            return(1)
        gp1=[]
    #/diagonally winner
    gp2=[]
    col=list(range(3))
    row=list(reversed(range(3)))
    for r,c in zip(row,col):
        gp2.append(box[r][c])
    if gp2.count(gp2[0])==len(box) and gp2[0] != 0:
        print(f"{gp2[0]} is winner diagonally")
        return (1)
    #\type diagonal
    gp4=[]
    for i,row in enumerate(box):
        gp4.append(row[i])
    if gp4.count(gp4[0])==len(box) and gp4[0]  != 0:
        print(f"{gp4[0]} is winner diagonally")
        return (1)
print("player 1 will start the game")
player=iter([1,2])
player=itertools.cycle(player)
count=0
flag1=0
play=True
while play == True:
    count +=1
    if count==9:
        print("the game is draw")
        play=False
    else:
        w=winner(box)
        if w==1:
            play=False

        rowchoice=int(input("enter the row choice from [0 , 1, 2]  "))
        columnchoice = int(input("enter the column choice from [0 , 1, 2]  "))

        if flag1==1:
            currentplayer=flag2

        else:
            currentplayer=next(player)
            print("\n the move played by ", currentplayer, "is: ")
            if box[rowchoice][columnchoice]!=0:
                print("position is already ocupied")
                flag1=1
                flag=box[rowchoice][columnchoice]
                if flag==1:
                    flag2=2
                else:
                    flag2=1

            else:
                box[rowchoice][columnchoice]= currentplayer


