import os
import sys
import inspect

def move_pwd_up() -> None:
    
    '''
        Move working directory up for 1 level.
    '''
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir) 