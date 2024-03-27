from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": "penske-chat-app-b53dd4f99ae3.herokuapp.com"}})

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/query')
def query():
    param = request.args.get('param', 'No parameter provided')
    return f"Received parameter: {param}"

if __name__ == '__main__':
    app.run(debug=True)