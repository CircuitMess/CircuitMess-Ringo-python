from RINGO import RINGO
import machine, time

mp = RINGO()

#test all buttons

while(1):
    for x in range(16):
        print(mp.buttons.readState(x))
        
    print(mp.buttons.readState(mp.BTN_A))
    print(mp.buttons.readState(mp.BTN_B))
    print(mp.buttons.readJoystickX())
    print(mp.buttons.readJoystickY())
    time.sleep_ms(250)
    mp.cls() #clear screen