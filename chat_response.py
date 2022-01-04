import re
import random
import json

with open('./responses.json', 'r', encoding = 'utf-8') as f:
    res_data = json.load(f)

def msg_probability(input_text: str, reconized_word: str, single_response: bool = False, required_words: list[str] = []) -> int:
    message_certainty = 0
    has_required_word = True
    
    for word in input_text:
        if word in reconized_word:
            message_certainty += 1
            
    percentage = float(message_certainty) / float(len(reconized_word))
    
    for word in required_words:
        if word not in input_text:
            has_required_word = False
            break
        
    if has_required_word or single_response:
        return int(percentage * 100)
    
    else:
        return 0
    
    
def check_all_msg(message: str):
    highest_prob_list = {}
    
    def response(bot_response: str, list_of_words: list[str], single_response: bool = False, required_words: list[str] = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = msg_probability(message, list_of_words, single_response, required_words)
        

    for res in res_data:
        response(
            res_data[res]['response'], 
            list_of_words = res_data[res]['list_of_words'], 
            single_response = res_data[res]['is_single_response'], 
            required_words = res_data[res]['required_word']
        )
        
    unknown_response = ['Could you re-phrase that?', '...', 'Sounds about right', 'What does that mean?']   
    best_match = max(highest_prob_list, key = highest_prob_list.get)
    
    return random.choice(unknown_response) if highest_prob_list[best_match] < 1 else best_match


def get_response(input_text: str) -> str:
    split_text = re.split(r'\s+|[,;?!.-]\s*', input_text.lower())
    response = check_all_msg(split_text)
    return response