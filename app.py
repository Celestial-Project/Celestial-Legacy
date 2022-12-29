from flask import Flask, request
from flask_cors import CORS, cross_origin

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from chat_response import get_response

debug = False

app = Flask(__name__)
cors = CORS(app)
limiter = Limiter(get_remote_address, app = app)

app.config['MAX_CONTENT_LENGTH'] = 1024

@cross_origin()
@limiter.limit('450/minute')
@app.route('/celestial-api', methods = ['POST'])
def send_response():
    
    body = request.get_json()
    
    if body is None or body['message'] == '':
        return ({}, 400)
    
    return ({'chat': get_response(body['message'])}, 200)


def main():

    if debug:   
        app.run(host = '0.0.0.0', port = 21250, debug = True)
        return

    from waitress import serve
    serve(app, host = '0.0.0.0', port = 21250)
    

if __name__ == '__main__':
    main()