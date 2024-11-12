#Cecily Strong ProficiencyTest: Rock, Paper, Scissors

import random
a1=' '
a2=' '
a3=' '
b1=' '
b2=' '
b3=' '
c1=' '
c2=' '
c3=' '
a1input='top left'
a2input='top middle'
a3input='top right'
b1input='middle left'
b2input='middle'
b3input='middle right'
c1input='bottom left'
c2input='bottom middle'
c3input='right middle'
winA=[a1,a2,a3]
winB=[b1,b2,b3]
winC=[c1,c2,c3]
win1=[a1,b1,c1]
win2=[a2,b2,c2]
win3=[a3,b3,c3]
winac1=[a1,b2,c3]
winac2=[a3,b2,b1]
winningnumbers=[winA,winB,winC,win1,win2,win3,winac1,winac2]
coordinatesinput=[a1input,a2input,a3input,b1input,b2input,b3input,c1input,c2input,c3input]
coordinates=[a1,a2,a3,b1,b2,b3,c1,c2,c3]
play=True
y=0
def board():
    def printboard(x1,x2,x3):
        def printrow(variable):
            underline = "\033[4m" 
            print(f"|{underline}",(variable),end='|')
        printrow(x1)
        printrow(x2)
        printrow(x3)
        print(' ')
    printboard(a1,a2,a3)
    printboard(b1,b2,b3)
    printboard(c1,c2,c3)
def Xturn():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global coordinates
    global coordinatesinput
    global a1input
    global a2input
    global a3input
    global b1input
    global b2input
    global b3input
    global c1input
    global c2input
    global c3input
    print("which square would you like?")
    X=input(', '.join(coordinatesinput))
    X.lower()
    print(X)
    if X=='top left' and a1==' ':
        a1='X'
        coordinatesinput.remove('top left')
    elif X=='top middle' and a2==' ':
        a2='X'
        coordinatesinput.remove('top middle')
    elif X=='top right' and a3==' ':
        a3='X'
        coordinatesinput.remove('top right')
    elif X=='middle left' and b1==' ':
        b1='X'
        coordinatesinput.remove('middle left')
    elif X=='middle' and b2==' ':
        b2='X'
        coordinatesinput.remove('middle')
    elif X=='middle right' and b3==' ':
        b3='X'
        coordinatesinput.remove('middle right')
    elif X=='bottom left' and c1==' ':
        c1='X'
        coordinatesinput.remove('bottom left')
    elif X=='bottom middle' and c2==' ':
        c2='X'
        coordinatesinput.remove('bottom middle')
    elif X=='bottom right' and c3==' ':
        c3='X'
        coordinatesinput.remove('bottom right')
    else:
        print("coordinate not valid")
        board()
        Xturn()
    board()
def Oturn():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global coordinates
    global coordinatesinput
    global a1input
    global a2input
    global a3input
    global b1input
    global b2input
    global b3input
    global c1input
    global c2input
    global c3input
    O=random.choice(coordinatesinput)
    if O=='top left':
        a1='O'
        coordinatesinput.remove('top left')
    elif O=='top middle':
        a2='O'
        coordinatesinput.remove('top middle')
    elif O=='top right':
        a3='O'
        coordinatesinput.remove('top right')
    elif O=='middle left':
        b1='O'
        coordinatesinput.remove('middle left')
    elif O=='middle':
        b2='O'
        coordinatesinput.remove('middle')
    elif O=='middle right':
        b3='O'
        coordinatesinput.remove('middle right')
    elif O=='bottom left':
        c1='O'
        coordinatesinput.remove('bottom left')
    elif O=='bottom middle':
        c2='O'
        coordinatesinput.remove('bottom middle')
    elif O=='bottom right':
        c3='O'
        coordinatesinput.remove('bottom right')
    board()
def reset():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global coordinates
    global coordinatesinput
    a1=' '
    a2=' '
    a3=' '
    b1=' '
    b2=' '
    b3=' '
    c1=' '
    c2=' '
    c3=' '
    coordinatesinput=[a1input,a2input,a3input,b1input,b2input,b3input,c1input,c2input,c3input]
    coordinates=[a1,a2,a3,b1,b2,b3,c1,c2,c3]
#"""
while play==True:
    reset()
    print("Lets play Tic-Tac-Toe!")
    board()
    winorlose=False
    while winorlose==False:
        Xturn()
        print('')
        if all in winA=='X' or all in winB=='X' or all in winC=='X' or all in win1=='X' or all in win2=='X' or all in win3=='X' or all in winac1=='X' or all in winac2=='X':
            print("You win!")
            winorlose=True
        elif (not a1==' ')and(not a2==' ')and(not a3==' ')and(not b1==' ')and(not b2==' ')and(not b3==' ')and(not c1==' ')and(not c2==' ')and(not c3==' '):
            print('its a tie!')
            winorlose=True
        else:
            Oturn()
            print('')
            if all in winA=='O' or all in winB=='O' or all in winC=='O' or all in win1=='O' or all in win2=='O' or all in win3=='O' or all in winac1=='O' or all in winac2=='O':
                print('You lose')
                winorlose=True
            elif (not a1==' ')and(not a2==' ')and(not a3==' ')and(not b1==' ')and(not b2==' ')and(not b3==' ')and(not c1==' ')and(not c2==' ')and(not c3==' '):
                print('its a tie!')
                winorlose=True
            else:
                continue
    else:
        playinput=input("play again? y/n")
        playinput.lower()
        if playinput=='y':
            play=True
        else:
            play=False
#"""