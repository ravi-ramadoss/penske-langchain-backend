from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": "https://penske-chat-app-b53dd4f99ae3.herokuapp.com/"}})

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/query')
def query():
    param = request.args.get('param', 'No parameter provided')
    response = jsonify({'some': param})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)