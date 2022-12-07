from tkinter import *

grid = ["0", "0", "0",
        "0", "0", "0",
        "0", "0", "0"]
playingPlayer = ["x"]
restartActive = [False]
xWins = [0]
oWins = [0]
draw = [0]

def Draw():
    btn1.config(text="")
    btn2.config(text="It's")
    btn3.config(text="")
    btn4.config(text="A")
    btn5.config(text="Dra")
    btn6.config(text="w!   ")
    btn7.config(text=" Pla")
    btn8.config(text="y ag")
    btn9.config(text="ain! ")
    restartActive[0] = True

def restart():
    btn1.config(text="")
    btn2.config(text="")
    btn3.config(text="")
    btn4.config(text="")
    btn5.config(text="")
    btn6.config(text="")
    btn7.config(text="")
    btn8.config(text="")
    btn9.config(text="")
    playingPlayer[0] = "x"
    grid[0] = "0"
    grid[1] = "0"
    grid[2] = "0"
    grid[3] = "0"
    grid[4] = "0"
    grid[5] = "0"
    grid[6] = "0"
    grid[7] = "0"
    grid[8] = "0"
    restartActive[0] = False
    draw[0] = 0

def xWin():
    btn1.config(text="")
    btn2.config(text="X")
    btn3.config(text="")
    btn4.config(text="W")
    btn5.config(text="O")
    btn6.config(text="N!")
    btn7.config(text=" Pla")
    btn8.config(text="y ag")
    btn9.config(text="ain! ")
    restartActive[0] = True
    xWins[0] = xWins[0] + 1
    window.title("Tic Tac Toe   ( X. " + str(xWins[0]) + ")   (O. " + str(oWins[0]) + ")")

def oWin():
    btn1.config(text="")
    btn2.config(text="O")
    btn3.config(text="")
    btn4.config(text="W")
    btn5.config(text="O")
    btn6.config(text="N!")
    btn7.config(text=" Pla")
    btn8.config(text="y ag")
    btn9.config(text="ain! ")
    restartActive[0] = True
    oWins[0] = oWins[0] + 1
    window.title("Tic Tac Toe   ( X. " + str(xWins[0]) + ")   (O. " + str(oWins[0]) + ")")

def win():
    if(grid[0] == "x" and grid[1] == "x" and grid[2] == "x"):
        xWin()
    elif(grid[3] == "x" and grid[4] == "x" and grid[5] == "x"):
        xWin()
    elif(grid[6] == "x" and grid[7] == "x" and grid[8] == "x"):
        xWin()
    elif(grid[0] == "x" and grid[3] == "x" and grid[6] == "x"):
        xWin()
    elif(grid[1] == "x" and grid[4] == "x" and grid[7] == "x"):
        xWin()
    elif(grid[2] == "x" and grid[5] == "x" and grid[8] == "x"):
        xWin()
    elif(grid[0] == "x" and grid[4] == "x" and grid[8] == "x"):
        xWin()
    elif(grid[2] == "x" and grid[4] == "x" and grid[6] == "x"):
        xWin()

    if(grid[0] == "o" and grid[1] == "o" and grid[2] == "o"):
        oWin()
    elif(grid[3] == "o" and grid[4] == "o" and grid[5] == "o"):
        oWin()
    elif(grid[6] == "o" and grid[7] == "o" and grid[8] == "o"):
        oWin()
    elif(grid[0] == "o" and grid[3] == "o" and grid[6] == "o"):
        oWin()
    elif(grid[1] == "o" and grid[4] == "o" and grid[7] == "o"):
        oWin()
    elif(grid[2] == "o" and grid[5] == "o" and grid[8] == "o"):
        oWin()
    elif(grid[0] == "o" and grid[4] == "o" and grid[8] == "o"):
        oWin()
    elif(grid[2] == "o" and grid[4] == "o" and grid[6] == "o"):
        oWin()

def press1():
    if(playingPlayer[0] == "x" and grid[0] == "0" and restartActive[0] == False):
        btn1.config(text="X")
        grid[0] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[0] == "0" and restartActive[0] == False):
        btn1.config(text="O")
        grid[0] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw()     

def press2():
    if(playingPlayer[0] == "x" and grid[1] == "0" and restartActive[0] == False):
        btn2.config(text="X")
        grid[1] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[1] == "0" and restartActive[0] == False):
        btn2.config(text="O")
        grid[1] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw() 

def press3():
    if(playingPlayer[0] == "x" and grid[2] == "0" and restartActive[0] == False):
        btn3.config(text="X")
        grid[2] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[2] == "0" and restartActive[0] == False):
        btn3.config(text="O")
        grid[2] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw() 

def press4():
    if(playingPlayer[0] == "x" and grid[3] == "0" and restartActive[0] == False):
        btn4.config(text="X")
        grid[3] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[3] == "0" and restartActive[0] == False):
        btn4.config(text="O")
        grid[3] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw() 

def press5():
    if(playingPlayer[0] == "x" and grid[4] == "0" and restartActive[0] == False):
        btn5.config(text="X")
        grid[4] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[4] == "0" and restartActive[0] == False):
        btn5.config(text="O")
        grid[4] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw() 

def press6():
    if(playingPlayer[0] == "x" and grid[5] == "0" and restartActive[0] == False):
        btn6.config(text="X")
        grid[5] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[5] == "0" and restartActive[0] == False):
        btn6.config(text="O")
        grid[5] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw() 

def press7():
    if(restartActive[0] == True):
        restart()
    elif(playingPlayer[0] == "x" and grid[6] == "0" and restartActive[0] == False):
        btn7.config(text="X")
        grid[6] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[6] == "0" and restartActive[0] == False):
        btn7.config(text="O")
        grid[6] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw() 

def press8():
    if(restartActive[0] == True):
        restart()
    elif(playingPlayer[0] == "x" and grid[7] == "0" and restartActive[0] == False):
        btn8.config(text="X")
        grid[7] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[7] == "0" and restartActive[0] == False):
        btn8.config(text="O")
        grid[7] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw() 

def press9():
    if(restartActive[0] == True):
        restart()
    elif(playingPlayer[0] == "x" and grid[8] == "0" and restartActive[0] == False):
        btn9.config(text="X")
        grid[8] = "x"
        playingPlayer[0] = "o"
        draw[0] +=1
        win()
    elif(playingPlayer[0] == "o" and grid[8] == "0"and restartActive[0] == False):
        btn9.config(text="O")
        grid[8] = "o"
        playingPlayer[0] = "x"
        draw[0] +=1
        win()
    if(draw[0] == 9):
        Draw()

window = Tk()

window.title("Tic Tac Toe   ( X. " + str(xWins[0]) + ")   (O. " + str(oWins[0]) + ")")
window.geometry("596x624")

icon = PhotoImage(file="project\\img\\x.gif")
window.iconphoto(True,icon)
window.config(background='#000')

btn1 = Button(window, text="", command = press1)
btn1.grid(row=1, column=1)
btn1.config(font=("Helvetica", 80))
btn1.config(width="3")
btn1.config(height="1")

btn2 = Button(window, text="", command = press2)
btn2.grid(row=1, column=2)
btn2.config(font=("Helvetica", 80))
btn2.config(width="3")
btn2.config(height="1")

btn3 = Button(window, text="", command = press3)
btn3.grid(row=1, column=3)
btn3.config(font=("Helvetica", 80))
btn3.config(width="3")
btn3.config(height="1")

btn4 = Button(window, text="", command = press4)
btn4.grid(row=2, column=1)
btn4.config(font=("Helvetica", 80))
btn4.config(width="3")
btn4.config(height="1")

btn5 = Button(window, text="", command = press5)
btn5.grid(row=2, column=2)
btn5.config(font=("Helvetica", 80))
btn5.config(width="3")
btn5.config(height="1")

btn6 = Button(window, text="", command = press6)
btn6.grid(row=2, column=3)
btn6.config(font=("Helvetica", 80))
btn6.config(width="3")
btn6.config(height="1")

btn7 = Button(window, text="", command = press7)
btn7.grid(row=3, column=1)
btn7.config(font=("Helvetica", 80))
btn7.config(width="3")
btn7.config(height="1")

btn8 = Button(window, text="", command = press8)
btn8.grid(row=3, column=2)
btn8.config(font=("Helvetica", 80))
btn8.config(width="3")
btn8.config(height="1")

btn9 = Button(window, text="", command = press9)
btn9.grid(row=3, column=3)
btn9.config(font=("Helvetica", 80))
btn9.config(width="3")
btn9.config(height="1")

window.mainloop()