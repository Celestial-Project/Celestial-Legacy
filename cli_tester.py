from chat_response import get_response

# run this file to test your chat intents on the terminal before commit

print('Press ctrl+c to exit.')

while True:
    
    try:
        print(get_response(input('#> '), debug = True))
        
    except KeyboardInterrupt:
        print('\nExited.')
        exit()