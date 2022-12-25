from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello world Flask'

@app.route('/nitesh')
def hello_world():
    return 'Hello, ' + request.args.get('name')