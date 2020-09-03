import sys,os
sys.path.append('.')

from PSignal import Signal
from threading import Thread
from time import sleep

class ThreadSig(Thread):

    def __init__(self):
        super().__init__()
        self.p = Signal()

    def run(self):
        sleep(3)
        self.p.emit(1,2,4)

class ThreadMain(Thread):
    def __init__(self,Number):
        super().__init__()
        self.Number = Number
        T1 = ThreadSig()
        T1.p.connect(self.func1)
        T1.p.connect(self.func2)
        T1.start()

    def func1(self,inp,out,h):
        print(f'hello {self.Number}-{inp,out}')
        sleep(1)
        print('Done')

    def func2(self,inp,out,h):
        print(f'hello {self.Number}-{inp,out}')
        sleep(1)
        print('Done')

    def run(self):
        sleep(10)

if __name__ == "__main__":
    [ThreadMain(i).start() for i in range(5)]
    
    # hello 0-(1, 2)
    # hello 0-(1, 2)
    # hello 1-(1, 2)
    # hello 2-(1, 2)
    # hello 1-(1, 2)
    # hello 2-(1, 2)
    # hello 3-(1, 2)
    # hello 4-(1, 2)
    # hello 3-(1, 2)
    # hello 4-(1, 2)
    # Done
    # Done
    # Done
    # Done
    # Done
    # Done
    # Done
    # Done
    # Done
    # Done