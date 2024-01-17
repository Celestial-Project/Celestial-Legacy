import os
import sys
import json
import inspect


def load_json(filename: str) -> dict:
    with open(filename, encoding = 'utf-8') as f:
        return json.load(f)
    
    
def move_pwd_up() -> None:
    
    '''
        Move working directory up for 1 level.
    '''
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir) 