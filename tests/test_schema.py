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
        

def test_schema_values() -> None:
    
    intents_en = test_utils.load_json('./responses/responses.json')
    intents_th = test_utils.load_json('./responses/responses_th.json')
    
    festival_en = test_utils.load_json('./responses/festivals.json')
    festival_th = test_utils.load_json('./responses/festivals_th.json')
    
    for (en, th) in zip(intents_en.keys(), intents_th.keys()):
        
        (current_en, current_th) = (intents_en[en], intents_th[th])
        
        assert current_en['response']
        assert current_th['response']
        
        assert current_en['list_of_words']
        assert current_th['list_of_words']
        
    for (en, th) in zip(festival_en.keys(), festival_th.keys()):
        
        (current_en, current_th) = (festival_en[en], festival_th[th])
        
        assert current_en['response']
        assert current_en['response']['fes']
        assert current_en['response']['nonfes']
        assert current_th['response']
        assert current_th['response']['fes']
        assert current_th['response']['nonfes']
        
        assert current_en['list_of_words']
        assert current_th['list_of_words']
        
        assert current_en['date']
        assert current_th['date']
        
        if isinstance(current_en['date'], list):
            assert current_en['date'][0] in range(1, 32)
            assert current_en['date'][1] in range(1, 32)
            assert current_en['date'][0] < current_en['date'][1]
            
        elif isinstance(current_en['date'], int):
            assert current_en['date'] in range(1, 32)
        
        if isinstance(current_th['date'], list):
            assert current_th['date'][0] in range(1, 32)
            assert current_th['date'][1] in range(1, 32)
            assert current_th['date'][0] < current_th['date'][1]
            
        elif isinstance(current_th['date'], int):
            assert current_th['date'] in range(1, 32)
            
        assert current_en['month']
        assert current_en['month'] in range(1, 13)
        assert current_th['month']
        assert current_th['month'] in range(1, 13)