from tkinter import *
from random import *
from tkinter import messagebox

mw = Tk()
mw.title("MINESWEEPER 101")
fcount= Label(mw, text = f"FLAGS ={0}")

mi_bomb = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\bomb.png").subsample(2,2)
mi_blank  = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\blank.png").subsample(8,8)
mi_flag  = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\flagged.png").subsample(8,8)
mi0 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\0.png").subsample(8,8)
mi1 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\1.png").subsample(8,8)
mi2 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\2.png").subsample(8,8)
mi3 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\3.png").subsample(8,8)
mi4 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\4.png").subsample(8,8)
mi5 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\5.png").subsample(8,8)
mi6 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\6.png").subsample(8,8)
mi7 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\7.png").subsample(8,8)
mi8 = PhotoImage(file = r"C:\Users\Sagar Annaji\Desktop\minesweeper-master\Images\8.png").subsample(8,8)


def exists(row, col):
    if(row in range(boardsize) and col in range(boardsize)):
        return (True)
    else:
        return (False)


def no_of_mines(row,col):
    count=0
    if(exists(row-1,col) == True):
        if(board[row-1,col]==1):
            count+=1
    if (exists(row + 1, col) == True):
        if (board[row + 1, col] == 1):
            count +=1
    if (exists(row, col-1) == True):
        if (board[row, col-1] == 1):
            count +=1
    if (exists(row, col+1) == True):
        if (board[row, col+1] == 1):
            count +=1
    if (exists(row-1, col+1) == True):
        if (board[row-1, col+1] == 1):
            count +=1
    if (exists(row-1, col-1) == True):
        if (board[row-1, col-1] == 1):
            count +=1
    if (exists(row+1, col+1) == True):
        if (board[row+1, col+1] == 1):
            count +=1
    if (exists(row+1, col-1) == True):
        if (board[row+1, col-1] == 1):
            count +=1
    return (count)



def zero(event,row,col):
    global flags_placed
    global flagged
    global revealed

    x = row
    y = col
    if (exists(row - 1, col) == True and revealed[row-1,col]== False):
        if (no_of_mines(row - 1, col) == 0):
            button[row - 1, col].config(image=mi0)
            revealed[x,y]=True
            zero(event,x - 1, y)
        else:
            check(event,row - 1, col)
    if (exists(row + 1, col) == True and revealed[row+1,col]== False):
        if (no_of_mines(row + 1, col) == 0):
            button[row + 1, col].config(image=mi0)
            revealed[x, y] = True
            zero(event,x + 1, y)
        else:
            check(event,row + 1, col)
    if (exists(row, col - 1) == True and revealed[row,col-1]== False):
        if (no_of_mines(row, col - 1) == 0):
            button[row, col - 1].config(image=mi0)
            revealed[x, y] = True
            zero(event,x, y-1)
        else:
            check(event,row, col - 1)
    if (exists(row, col + 1) == True and revealed[row,col+1]== False):
        if (no_of_mines(row, col + 1) == 0):
            button[row, col + 1].config(image=mi0)
            revealed[x, y] = True
            zero(event,x, y+1)
        else:
            check(event,row, col + 1)
    if (exists(row - 1, col + 1) == True and revealed[row-1,col+1]== False):
        if (no_of_mines(row - 1, col + 1) == 0):
            button[row - 1, col + 1].config(image=mi0)
            revealed[x, y] = True
            zero(event,x - 1, y+1)
        else:
            check(event,row-1,col+1)
    if (exists(row - 1, col - 1) == True and revealed[row-1,col-1]== False):
        if (no_of_mines(row - 1, col - 1) == 0):
            button[row - 1, col - 1].config(image=mi0)
            revealed[x, y] = True
            zero(event,x - 1, y-1)
        else:
            check(event,row - 1, col - 1)
    if (exists(row + 1, col + 1) == True and revealed[row+1,col+1]== False):
        if (no_of_mines(row + 1, col + 1) == 0):
            button[row + 1, col + 1].config(image=mi0)
            revealed[x, y] = True
            zero(event,x + 1, y+1)
        else:
            check(event,row + 1, col + 1)
    if (exists(row + 1, col - 1) == True and revealed[row+1,col-1]== False):
        if (no_of_mines(row + 1, col - 1) == 0):
            button[row + 1, col - 1].config(image=mi0)
            revealed[x, y] = True
            zero(event,x + 1, y-1)
        else:
            check(event,row + 1, col - 1)

    if flagged[(row, col)] == True and revealed[row, col] == True:
        flags_placed -= 1
        flagged[row, col] = False
        fcount.config(text=f"FLAGS ={flags_placed}")
        #print(flags_placed)


def check(event,x,y):
    global flags_placed
    global flagged
    global revealed
    if (board[x, y] == 1):
        for i in bomb_index:
            button[i].config(image = mi_bomb)
        if messagebox.showinfo("Result","CHI CHI YOU LOST") :
            #mw.destroy()
            startgame(boardsize,no_of_mines_to_be_placed)
    else:
        mine_count = no_of_mines(x,y)

        if(mine_count == 0):
            row=x
            col=y
            #adj = [(row - 1, col),(row + 1, col),(row, col - 1),(row, col + 1),(row - 1, col + 1),(row - 1, col - 1),(row + 1, col + 1),(row + 1, col - 1)]
            button[x, y].config(image=mi0)
            revealed[x,y]= True
            zero(event,x,y)
        if(mine_count == 1):
            button[x, y].config(image = mi1)
            revealed[x, y] = True
        if (mine_count == 2):
            button[x, y].config(image = mi2)
            revealed[x, y] = True
        if (mine_count == 3):
            button[x, y].config(image=mi3)
            revealed[x, y] = True
        if (mine_count == 4):
            button[x, y].config(image=mi4)
            revealed[x, y] = True
        if (mine_count == 5):
            button[x, y].config(image=mi5)
            revealed[x, y] = True
        if (mine_count == 6):
            button[x, y].config(image=mi6)
            revealed[x, y] = True
        if (mine_count == 7):
            button[x, y].config(image=mi7)
            revealed[x, y] = True
        if (mine_count == 8):
            button[x, y].config(image=mi8)
            revealed[x, y] = True
        if flagged[(x, y)] == True and revealed[x, y] == True:
            flags_placed -= 1
            flagged[x, y] = False
            fcount.config(text=f"FLAGS ={flags_placed}")
            #print(flags_placed)



def rightclick(event,row,col):
    global identified_bombs
    global flags_placed
    global flag_index
    global boardsize
    flag_index = {}
    if(revealed[row,col]==False and flagged[(row,col)]==False):
        button[row,col].config(image=mi_flag)
        flagged[row,col] = True
        flags_placed += 1
        fcount.config(text=f"FLAGS ={flags_placed}")
        #print(flags_placed)
        if((row,col) in bomb_index):
            identified_bombs+=1
            #print(identified_bombs)

    elif(flagged[(row,col)]==True):
        button[row,col].config(image=mi_blank)
        flagged[row,col]=False
        flags_placed -= 1
        fcount.config(text=f"FLAGS ={flags_placed}")
        #print(flags_placed)
        if((row,col) in bomb_index):
            identified_bombs-=1
            #print(identified_bombs)


    if(identified_bombs == no_of_mines_to_be_placed and flags_placed == no_of_mines_to_be_placed):
        if messagebox.showinfo("Result","YOU WON!!") :
            #mw.destroy()
            startgame(boardsize, no_of_mines_to_be_placed)

def startgame(size =10, bombs = 10):
    widget_list = mw.winfo_children()
    for item in widget_list:
        item.grid_forget()

    global button
    global board
    global revealed
    global flagged
    global bomb_index

    global boardsize
    global no_of_mines_to_be_placed
    global identified_bombs
    global flags_placed

    boardsize = size
    no_of_mines_to_be_placed = bombs
    flags_placed = 0
    identified_bombs = 0

    menubar = Menu(mw)
    menubar.add_command(label="Restart", command=lambda size=boardsize, bombs=no_of_mines_to_be_placed: startgame(size, bombs))
    difficulty = Menu(tearoff=0)
    difficulty.add_command(label="Easy 10x10 bombs = 10", command=lambda size=10, bombs=10: startgame(size, bombs))
    difficulty.add_command(label="Medium 14x14 bombs = 30", command=lambda size=13, bombs=30: startgame(size, bombs))
    difficulty.add_command(label="Hardcore AF 16x16 bombs = 69", command=lambda size=16, bombs=69: startgame(size, bombs))
    menubar.add_cascade(label="Difficulty", menu=difficulty)
    mw.config(menu=menubar)
    fcount.config(text=f"FLAGS ={flags_placed}")

    button = {}
    board = {}
    revealed = {}
    flagged = {}
    bomb_index = set()

    #fr = Frame(mw, height = 300, width = 300).grid()
    for row in range(boardsize):
        for col in range(boardsize):
            board[(row, col)] = 0
            revealed[(row, col)] = False
            flagged[(row, col)] = False

    while (len(bomb_index) != no_of_mines_to_be_placed):
        x = randrange(boardsize)
        y = randrange(boardsize)
        bomb_index.add((x, y))
        board[x, y] = 1

    for row in range(boardsize):
        for col in range (boardsize):
            button[row,col] = Button(mw)#, command = lambda x=row, y=col : check(x,y))
            button[row,col].bind("<Button-1>", lambda event, x=row, y=col : check(event,x,y))
            button[row, col].bind("<Button-3>", lambda event, x=row,y=col : rightclick(event,x,y))
            button[row,col].config(image = mi_blank)
            button[row,col].grid(row = row,column = col)
    fcount.grid(columnspan = 3)


startgame()
mainloop()
