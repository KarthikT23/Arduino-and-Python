import pyfirmata
import time
from winsound import Beep
#---------------------------------------
board = pyfirmata.Arduino("COM12")
#---------------------------------------
board.digital[2].mode = pyfirmata.INPUT  
it = pyfirmata.util.Iterator(board)  
it.start()
#---------------------------------------
print("\nALARM OFF")
while True:
    alarm = board.digital[2].read()
    if alarm == True:
        print("\nALARM ON")
        for i in range(10):
            Beep(500,700)
            board.digital[3].write(1)
            time.sleep(0.05)
            board.digital[3].write(0)
            time.sleep(0.05)
        print("\nALARM OFF")