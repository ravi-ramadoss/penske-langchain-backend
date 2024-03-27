from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/query')
def query():
    param = request.args.get('param', 'No parameter provided')
    response = "haha"
    return response

if __name__ == '__main__':
    app.run(debug=True)