import pytest

from utils import move_pwd_up

move_pwd_up()

from main import use_debug_mode

def test_is_debug_mode_on():

    assert not use_debug_mode, '\u001b[41;1m !! \u001b[0m Error: Discord bot debug mode need to be turn off before pushing.'