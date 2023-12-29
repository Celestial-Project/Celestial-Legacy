import json

from test_utils import move_pwd_up

move_pwd_up()

from chat_response import get_response


def test_intents_th():
    get_response('hi')
    get_response('christmas')
    
    
def test_intents_en():
    get_response('สวัสดี')
    get_response('ปีใหม่')