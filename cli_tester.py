import os 
import sys
from chat_response import get_response

# run this file to test your chat intents on the terminal before commit

print('\u001b[45;1m ** \u001b[0m Welcome to Celestial command-line testing interface!')
print('\u001b[45;1m ** \u001b[0m Press ctrl+c to exit.')

while True:
    
    try:
        
        inp = input('\u001b[47;1m #> \u001b[0m ')
        
        # Reload the engine on command
        if inp == '--reload' or inp == '-r':
            os.system('clear')
            print('\u001b[45;1m ** \u001b[0m Reloading...')
            os.execl(sys.executable, sys.executable, *sys.argv)
                  
        else:
            get_response(inp, debug = True)
        
    except KeyboardInterrupt:
        print('\n\u001b[45;1m ** \u001b[0m Exiting test mode...')
        exit()