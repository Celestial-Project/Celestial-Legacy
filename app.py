import os
from flask import Flask, request
from flask_cors import CORS, cross_origin

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from logger import info_log
from chat_response import get_response

debug = False

app = Flask(__name__)
cors = CORS(app)
limiter = Limiter(key_func = get_remote_address, app = app)

app.config['MAX_CONTENT_LENGTH'] = 1024

def show_ready(port: int, debug: bool) -> None:

    os.system('cls' if os.name == 'nt' else 'clear')
    
    info_log('Chat REST API ready!')
    info_log(f'Mode: {"Debug" if debug else "Production"}')
    info_log('Press ctrl+c to exit.')
    info_log(f'API running on: http://localhost:{port}')


@cross_origin()
@limiter.limit('450/minute')
@app.route('/celestial-api', methods = ['POST'])
def send_response():
    
    body = request.get_json()
    
    if body is None or body['message'] == '':
        return ({}, 400)
    
    return ({'chat': get_response(body['message'])}, 200)


def main():

    PORT = 21250

    if debug:  

        show_ready(PORT, debug)

        app.run(host = '0.0.0.0', port = PORT)
        return

    from waitress import serve
    
    show_ready(PORT, debug)
    serve(app, host = '0.0.0.0', port = PORT)
    

if __name__ == '__main__':
    main()