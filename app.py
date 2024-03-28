from flask import Flask, request, jsonify
from langchainservice import get_response

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/query')
def query():
    question = request.args.get('question')
    #, 'No parameter provided')
    print(f"question is {question}")
    response = get_response(question)
    return response

if __name__ == '__main__':
    app.run(debug=True)