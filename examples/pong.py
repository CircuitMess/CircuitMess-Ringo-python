from RINGO import RINGO
mp = RINGO()
import random, utime
paused = False
#player variables
player_score = 0
player_h = 32
player_w = 6
player_x = 0
player_y = (128 - player_h) / 2
player_vy = 2
#oponent variables
oponent_score = 0
oponent_h = 32
oponent_w = 6
oponent_x = 160 - oponent_w
oponent_y = (128 - oponent_h) / 2
oponent_vy = 2
#ball variables
ball_size = 12
ball_x = 160 - ball_size - oponent_w - 1
ball_y = (128 - ball_size) / 2
ball_vx = 3
ball_vy = 3

#def text( self, aPos, aString, aColor = BLACK, aFont, aSize = 1, nowrap = False ) :
random.seed(utime.ticks_ms()*utime.ticks_ms())
while (1):
    
    if (mp.buttons.readState(mp.BTN_A)):
        while (mp.buttons.readState(mp.BTN_A)):
            pass
        mp.display.fill(0)
        mp.display.text((50, 57), "PAUSED", mp.WHITE, mp.font1, 2)
        while (not mp.buttons.readState(mp.BTN_A)):
            pass
        while (mp.buttons.readState(mp.BTN_A)):
            pass
    
    if (mp.buttons.readJoystickX() < 100):
        mp.display.rect((player_x, player_y), (player_w, player_h), mp.BLACK)
        player_y = max(0, player_y - player_vy)
    if (mp.buttons.readJoystickX() > 1000):
        mp.display.rect((player_x, player_y), (player_w, player_h), mp.BLACK)
        player_y = min(128 - player_h, player_y + player_vy)

    mp.display.rect((ball_x, ball_y), (ball_size, ball_size), mp.BLACK)
    ball_x += ball_vx
    ball_y += ball_vy

    #check for ball collisions
	#collision with the top border
    if (ball_y < 0):
        ball_y = 0
        ball_vy = -ball_vy
    #collision with the bottom border
    if (ball_y + ball_size) > 128:
        ball_y = 128 - ball_size
        ball_vy = -ball_vy
    #collision with the player
    if (mp.collideRectRect(ball_x, ball_y, ball_size, ball_size, player_x, player_y, player_w, player_h)):
        ball_x = player_x + player_w
        ball_vx = -ball_vx
    if mp.collideRectRect(ball_x, ball_y, ball_size, ball_size, oponent_x, oponent_y, oponent_w, oponent_h):
        ball_x = oponent_x - ball_size
        ball_vx = -ball_vx

    if (ball_x < 0) :
        oponent_score = oponent_score + 1
        ball_x = 160 - ball_size - oponent_w - 1
        ball_vx = -abs(ball_vx)
        ball_y = random.randint(0, 128 - ball_size)

    if ((ball_x + ball_size) > 160):
        player_score = player_score + 1
        #mp.sound.playOK()
        ball_x = 160 - ball_size - oponent_w - 16 #place the ball on the oponent side
        ball_vx = -abs(ball_vx)
        ball_y = random.randint(0, 128 - ball_size)

    if ((player_score == 10) or (oponent_score == 10)):
        player_score = 0
        oponent_score = 0
    
    #move the oponent
    if ((oponent_y + (oponent_h / 2)) < (ball_y + (ball_size / 2))):  #if the ball is below the oponent
        mp.display.rect((oponent_x, oponent_y), (oponent_w, oponent_h), mp.BLACK)
        oponent_y = oponent_y + oponent_vy #move down
        oponent_y = min(128 - oponent_h, oponent_y) #don't go out of the screen
    else:
        mp.display.rect((oponent_x, oponent_y), (oponent_w, oponent_h), mp.BLACK)
        oponent_y = oponent_y - oponent_vy #move up
        oponent_y = max(0, oponent_y)  #don't go out of the screen

   # mp.display.text((15,16), str(player_score), mp.WHITE, mp.font1, 2)
   # mp.display.text((57, 16), str(oponent_score), mp.WHITE, mp.font1, 2)
    #draw the ball
    mp.display.rect((ball_x, ball_y), (ball_size, ball_size), mp.WHITE)
    #draw the player
    mp.display.rect((player_x, player_y), (player_w, player_h), mp.RED)
    #draw the oponent
    mp.display.rect((oponent_x, oponent_y), (oponent_w, oponent_h), mp.BLUE)
    
            
    
        