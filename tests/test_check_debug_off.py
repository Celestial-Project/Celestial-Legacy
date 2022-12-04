import os
import sys
import pytest
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from main import use_debug_mode

def test_is_debug_mode_on():

    assert not use_debug_mode, '\u001b[41;1m !! \u001b[0m Error: Discord bot debug mode need to be turn off before pushing.'