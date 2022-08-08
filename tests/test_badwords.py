import os
import sys
import json
import pytest
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from chat_response import get_response

with open('./responses/badwords.json') as f:
    bw = json.load(f)
    
en_rude_sentences = [
    'fuck you',
    'motherfucker',
    'you fucking cunt',
    'shut the fuck up',
    'why you so stupid'
]

th_rude_sentences = [
    'ควยไรสัส',
    'เย็ดแม่',
    'โง่',
    'กากว่ะ',
    'เงี่ยนว่ะ'
]

def test_badwords_th():
    
    response = 'แบบนี้ไม่ดีเลยนะคะ เอาเป็นว่าคุณพี่ใจเย็นๆ แล้วค่อยมาคุยกันดีๆ ดีกว่านะคะ'
    
    for sen in th_rude_sentences:
        assert get_response(sen) == response
    
    
def test_badwords_en():
    
    response = 'I\'m sorry you feel that way. I think you calm down just a little bit.'
    
    for sen in en_rude_sentences:
        assert get_response(sen) == response