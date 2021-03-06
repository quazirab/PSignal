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
        print(f'func1 {self.Number}-{inp,out}')
        sleep(1)
        print('Done - func1')

    def func2(self,inp,out,h):
        print(f'func2 {self.Number}-{inp,out}')
        sleep(1)
        print('Done - func2')

    def run(self):
        sleep(10)

if __name__ == "__main__":
    [ThreadMain(i).start() for i in range(5)]
    
    # func1 0-(1, 2)
    # func2 0-(1, 2)
    # func1 1-(1, 2)
    # func1 2-(1, 2)
    # func1 4-(1, 2)
    # func2 1-(1, 2)
    # func1 3-(1, 2)
    # func2 3-(1, 2)
    # func2 4-(1, 2)
    # func2 2-(1, 2)
    # Done - func1
    # Done - func2
    # Done - func1
    # Done - func1
    # Done - func1
    # Done - func2
    # Done - func2
    # Done - func1
    # Done - func2
    # Done - func2