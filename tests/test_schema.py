import test_utils

def test_schema_keys() -> None:
    
    intents_en = test_utils.load_json('./responses/responses.json')
    intents_th = test_utils.load_json('./responses/responses_th.json')
    
    festival_en = test_utils.load_json('./responses/festivals.json')
    festival_th = test_utils.load_json('./responses/festivals_th.json')
    
    
    for (en, th) in zip(intents_en.keys(), intents_th.keys()):
        (current_en, current_th) = (intents_en[en], intents_th[th])
        assert {'response', 'list_of_words', 'is_single_response', 'required_word'} == set(current_en.keys())
        assert {'response', 'list_of_words', 'is_single_response', 'required_word'} == set(current_th.keys())
    
    for (en, th) in zip(festival_en.keys(), festival_th.keys()):
        
        (current_en, current_th) = (festival_en[en], festival_th[th])
        
        assert {'response', 'list_of_words', 'is_single_response', 'required_word', 'date', 'month'} == set(current_en.keys())
        assert {'response', 'list_of_words', 'is_single_response', 'required_word', 'date', 'month'} == set(current_th.keys())
        
        (inner_en, inner_th) = (festival_en[en]['response'], festival_th[th]['response'])
        
        assert {'fes', 'nonfes'} == set(inner_en.keys())
        assert {'fes', 'nonfes'} == set(inner_th.keys())
