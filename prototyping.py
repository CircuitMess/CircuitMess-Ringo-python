from MAKERphone import MAKERphone
import utime
mp = MAKERphone()
mp.display.fill(mp.BLACK)
# mp.display.text((0,0), "HELLO WORLD", mp.WHITE, mp.font1)
while (1):
    # if (mp.buttons.read(mp.BTN_A)):
    #     mp.display.fill(mp.RED)
    # else:
    #     mp.display.fill(mp.BLACK)
    time.delay_ms(1000)
    print()