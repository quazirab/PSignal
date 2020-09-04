from threading import Thread
from time import time,sleep

class Signal(object): 
    '''
    The Signal class creates callback signal for other classes using threading
    
    Attributes:
        None

    '''
    def __init__(self):    
        super(Signal).__init__()
        self._slots = []

    def connect(self,func):
        '''
        Connects the func method to slot

        Args:
            func (method): function to add in callback slots
        
        Returns:
            None
        '''

        if not callable(func):
            raise TypeError('Signal must be connected to a method')
        self._slots.append(func)

    def disconnect(self,func):
        '''
        Disconnects the func method from slot

        Args:
            func (method): function to delete from callback slots

        Returns:
            None
        '''
        try:
            self._slots.remove(func)
        except ValueError:
            raise ValueError(f'{func} is not connected')

    def emit(self,*args, **kwargs):
        '''
        Runs all the connected slots with threads

        Args:
            *args: The variable arguments are used for the method
            **kwargs: The keyword arguments are used for the method
        Returns:
            None
        '''
        for slot in self._slots:
            Thread(target=slot,args=args,kwargs=kwargs).start()

class SignalFactory(dict):
    '''
    The SignalFactory class creates collection of callback signal for other classes using threading
    
    Attributes:
        None

    '''
    def register(self,name:str):
        '''
        Adds a Signal class to self dictionary
        
        Args:
            name: string , name of the signal
        
        Returns:
            None
        '''
        self[name] = Signal()

    def deregister(self,name:str):
        '''
        Removes the Signal class to self dictionary 

        Args:
            name: string , name of the signal
        
        Returns:
            None

        '''
        try:
            del self[name]
        except KeyError:
            raise KeyError(f'{name} does not exist')

class SignalTimer(Thread):
    '''
    The SignalTimer class finished emits signal after every n seconds.
    
    Attributes:
        s = time in seconds (default = 1 second)

    '''
    def __init__(self,s:float=1):
        super().__init__()
        self._s = s
        self._t = 0
        self._pause = 0
        self.started = Signal()
        self.finished = Signal()
        self._loop = 0

    def set_loop(self):
        '''
        Sets the timer in loop

        Args:
            None
        
        Returns:
            None

        '''

        self._loop = 1

    def set_time(self,s:float):
        '''
        Sets the timer time in seconds

        Args:
            None
        
        Returns:
            None

        '''
        self._s = s

    def pause(self):
        '''
        Pauses the timer

        Args:
            None
        
        Returns:
            None

        '''
        self._pause = 1
    
    def run(self):
        '''
        Runs the timer in a thread

        Args:
            None
        
        Returns:
            None

        '''
        self._pause = 0
        self.started.emit()
        if self._t == 0:
            self._t = time()
        while not self._pause:
            if time()-self._t >= self._s:
                self._t = time()
                self.finished.emit()
                if not self._loop:
                    self._pause = 1
            sleep(0.05)
    



    