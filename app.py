import os

from flask import Flask, request
from flask_cors import CORS, cross_origin

from chat_response import get_response

app = Flask(__name__)
cors = CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 1024

@app.route('/celestial-api', methods = ['POST'])
@cross_origin()
def send_response():
    
    if request.method == 'POST':
        body = request.get_json()
        
        print(body)
        
        return ({'chat': get_response(body['message'])}, 200) if body is not None else ({}, 401)
    

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = int(os.environ.get('PORT', 8080)))