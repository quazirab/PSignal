import sys,os
sys.path.append('.')

from PSignal import SignalTimer
from threading import Thread
from time import sleep,time

t = None
def TimerStarted():
    global t 
    t = time()
    print(f'Timer Started')

def TimerFinished():
    print(f'Timer Finished- {round(time()-t,0)}')


SigTim = SignalTimer()
SigTim.started.connect(TimerStarted)
SigTim.finished.connect(TimerFinished)
SigTim.set_loop()
SigTim.start()

sleep(10)
SigTim.pause()



# Timer Started
# Timer Finished- 1.0
# Timer Finished- 2.0
# Timer Finished- 3.0
# Timer Finished- 4.0
# Timer Finished- 5.0
# Timer Finished- 6.0
# Timer Finished- 7.0
# Timer Finished- 8.0
# Timer Finished- 9.0