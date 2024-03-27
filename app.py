from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/query')
def query():
    param = request.args.get('param', 'No parameter provided')
    return f"Received parameter: {param}"

if __name__ == '__main__':
    app.run(debug=True)