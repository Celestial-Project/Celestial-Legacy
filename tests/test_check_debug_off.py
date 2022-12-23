import pytest

from utils import move_pwd_up

move_pwd_up()

from main import use_debug_mode
from app import debug

def test_check_debug_main():
    assert not use_debug_mode, '\u001b[41;1m !! \u001b[0m Error: Discord bot debug mode need to be turn off before pushing.'


def test_check_debug_api():
    assert not debug, '\u001b[41;1m !! \u001b[0m Error: API debug mode need to be turn off before pushing.'