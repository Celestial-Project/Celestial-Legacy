from chat_response import get_response

# run this file to test your chat intents on the terminal before commit

print('\u001b[45;1m ** \u001b[0m Welcome to Celestial commnad-line testing interface!')
print('\u001b[45;1m ** \u001b[0m Press ctrl+c to exit.')

while True:
    
    try:
        get_response(input('\u001b[47;1m #> \u001b[0m '), debug = True)
        
    except KeyboardInterrupt:
        print('\n\u001b[45;1m ** \u001b[0m Exiting test mode...')
        exit()