import os 
import chat_response
from importlib import reload

# run this file to test your chat intents on the terminal before commit

print('\u001b[45;1m ** \u001b[0m Welcome to Celestial command-line testing interface!')
print('\u001b[45;1m ** \u001b[0m Type -h or --help to see list of test macro and controls.')
print('\u001b[45;1m ** \u001b[0m Press ctrl+c to exit.')

while True:
    
    try:
        
        inp = input('\u001b[47;1m #> \u001b[0m ')
        
        if inp == '--help' or inp == '-h':
            print('''
                  \u001b[43;1m macro \u001b[0m -h --help \t Show this help message.
                  \u001b[43;1m macro \u001b[0m -r --reload \t Reload the chat module.
                  \u001b[41;1m  ctl  \u001b[0m ^C ctrl+c \t Quit the program.
                  ''')
        
        # Reload the engine on command
        elif inp == '--reload' or inp == '-r':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\u001b[45;1m ** \u001b[0m Reloading...')
            reload(chat_response)
                  
        else:
            chat_response.get_response(inp, debug = True)
        
    except KeyboardInterrupt:
        print('\n\u001b[45;1m ** \u001b[0m Exiting test mode...')
        exit()