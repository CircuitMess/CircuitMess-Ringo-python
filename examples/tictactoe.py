from RINGO import RINGO
mp = RINGO()
field = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def print_cursor(turn, cursorX, cursorY, color):
    if(turn == 0):
        if (cursorY == 0):
            if (cursorX == 0):
                mp.display.line((16, 4), (54, 41), color)
                mp.display.line((54, 4), (16, 41), color)
            elif (cursorX == 1):
                mp.display.line((62, 4), (100, 41), color)
                mp.display.line((100, 4), (62, 41), color)
            else:
                mp.display.line((108, 4), (146, 41), color)
                mp.display.line((146, 4), (108, 41), color)

        elif (cursorY == 1):
            if (cursorX == 0):
                mp.display.line((16, 46), (54, 83), color)
                mp.display.line((54, 46), (16, 83), color)
            elif (cursorX == 1):
                mp.display.line((62, 46), (100, 83), color)
                mp.display.line((100, 46), (62, 83), color)
            else:
                mp.display.line((108, 46), (146, 83), color)
                mp.display.line((146, 46), (108, 83), color)

        else:
            if (cursorX == 0):
                mp.display.line((16, 88), (54, 125), color)
                mp.display.line((54, 88), (16, 125), color)
            elif (cursorX == 1):
                mp.display.line((62, 88), (100, 125), color)
                mp.display.line((100, 88), (62, 125), color)
            else:
                mp.display.line((108, 88), (146, 125), color)
                mp.display.line((146, 88), (108, 125), color)

    elif(turn == 1):
        if (cursorY == 0):
            if (cursorX == 0):
                mp.display.circle((35,22), 19, color)
            elif (cursorX == 1):
                 mp.display.circle((81,22), 19, color)
            else:
                 mp.display.circle((127,22), 19, color)

        elif (cursorY == 1):
            if (cursorX == 0):
                mp.display.circle((35,64), 19, color)
            elif (cursorX == 1):
                mp.display.circle((81,64), 19, color)
            else:
                mp.display.circle((127,64), 19, color)

        else:
            if (cursorX == 0):
                mp.display.circle((35,106), 19, color)
            elif (cursorX == 1):
                mp.display.circle((81,106), 19, color)
            else:
                mp.display.circle((127,106), 19, color)

def check_win(field):
    #Draw
    draw = True
    for i in range(3):
        for j in range(3):
            if (field[i][j] == ''):
                draw = False
    if (draw):
        return 'D'
    #Horizontal
    if (field[0][0] != ''):
        if (field[0][0] == field[0][1] and field[0][0] == field[0][2]):
            if (field[0][0] == 'X'):
                return 'X'
            else:
                return 'O'
    elif (field[1][0] != ''):
        if (field[1][0] == field[1][1] and field[1][0] == field[1][2]):
            if (field[1][0] == 'X'):
                return 'X'
            else:
                return 'O'
    elif (field[2][0] != ''):
        if (field[2][0] == field[2][1] and field[2][0] == field[2][2]):
            if (field[2][0] == 'X'):
                return 'X'
            else:
                return 'O'
    #Vertical
    if (field[0][0] != ''):
        if (field[0][0] == field[1][0] and field[0][0] == field[2][0]):
            if (field[0][0] == 'X'):
                return 'X'
            else:
                return 'O'
    elif (field[0][1] != ''):
        if (field[0][1] == field[1][1] and field[0][1] == field[2][1]):
            if (field[1][0] == 'X'):
                return 'X'
            else:
                return 'O'
    elif (field[0][2] != ''):
        if (field[0][2] == field[1][2] and field[0][2] == field[2][2]):
            if (field[2][0] == 'X'):
                return 'X'
            else:
                return 'O'
    #Diagonal
    if (field[0][0] != ''):
        if (field[0][0] == field[1][1] and field[0][0] == field[2][2]):
            if (field[0][0] == 'X'):
                return 'X'
            else:
                return 'O'
    elif (field[0][2] != ''):
        if (field[0][2] == field[1][1] and field[0][2] == field[2][0]):
            if (field[0][2] == 'X'):
                return 'X'
            else:
                return 'O'
    return ''

turn = 0
cursorX = 1
cursorY = 1
while (1):
    mp.display.vline((57, 2), 124, mp.WHITE)
    mp.display.vline((104, 2), 124, mp.WHITE)
    mp.display.hline((14, 43), 132, mp.WHITE)
    mp.display.hline((14, 86), 132, mp.WHITE)
    if(field[cursorY][cursorX] == ''):
        print_cursor(turn, cursorX, cursorY, mp.WHITE)
    if (turn == 0):
        # mp.display.fillrect((0, 0), (10, 10), mp.BLACK)
        mp.display.text((0, 0), "P1", mp.WHITE, mp.font1)

    else:
        # mp.display.fillrect((0, 0), (10, 10), mp.BLACK)
        mp.display.text((0, 0), "P2", mp.WHITE, mp.font1)

        
    if (mp.buttons.readJoystickY() > 1000 and cursorX > 0):
        if(field[cursorY][cursorX] == ''):
            print_cursor(turn, cursorX, cursorY, mp.BLACK)
        cursorX -= 1
        # while (mp.buttons.read(mp.BTN_LEFT)):
        #     pass
    if (mp.buttons.readJoystickY() < 100 and cursorX < 2):
        if(field[cursorY][cursorX] == ''):
            print_cursor(turn, cursorX, cursorY, mp.BLACK)
        cursorX += 1
        # while (mp.buttons.read(mp.BTN_RIGHT)):
        #     pass
    if (mp.buttons.readJoystickX() < 100 and cursorY > 0):
        if(field[cursorY][cursorX] == ''):
            print_cursor(turn, cursorX, cursorY, mp.BLACK)
        cursorY -= 1
        # while (mp.buttons.read(mp.BTN_UP)):
        #     pass
    if (mp.buttons.readJoystickX() > 1000 and cursorY < 2):
        if(field[cursorY][cursorX] == ''):
            print_cursor(turn, cursorX, cursorY, mp.BLACK)
        cursorY += 1
        # while (mp.buttons.read(mp.BTN_DOWN)):
        #     pass
    if (mp.buttons.readState(mp.BTN_A) and field[cursorY][cursorX] == ''):
        while (mp.buttons.readState(mp.BTN_A)):
            pass
        if (turn):
            field[cursorY][cursorX] = 'O'
        else:
            field[cursorY][cursorX] = 'X'
        turn = not turn
        mp.display.fillrect((0, 0), (15, 10), mp.BLACK)
        win = check_win(field)
        if (win == 'X'):
            mp.display.fill(0)
            mp.display.text((40, 50), "X wins!", mp.WHITE, mp.font1, 2)
            while (not mp.buttons.readState(mp.BTN_A)):
                pass
            field = [
                ['', '', ''],
                ['', '', ''],
                ['', '', '']
            ]
            mp.display.fill(0)
            cursorX = 1
            cursorY = 1

        elif (win == 'O'):
            mp.display.fill(0)
            mp.display.text((40, 50), "O wins!", mp.WHITE, mp.font1, 2)
            while (not mp.buttons.readState(mp.BTN_A)):
                pass
            field = [
                ['', '', ''],
                ['', '', ''],
                ['', '', '']
            ]
            mp.display.fill(0)
            cursorX = 1
            cursorY = 1
        elif (win == 'D'):
            mp.display.fill(0)
            mp.display.text((40, 50), "Draw!", mp.WHITE, mp.font1, 2)
            while (not mp.buttons.readState(mp.BTN_A)):
                pass
            field = [
                ['', '', ''],
                ['', '', ''],
                ['', '', '']
            ]
            mp.display.fill(0)
            cursorX = 1
            cursorY = 1
