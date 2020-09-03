from threading import Thread

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
        self._slots.append(func)

    def disconnect(self,func):
        '''
        Disconnects the func method from slot

        Args:
            func (method): function to delete from callback slots

        Returns:
            None
        '''
        self._slots.remove(func)

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