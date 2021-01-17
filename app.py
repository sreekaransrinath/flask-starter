from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>Hello, World!<h1>
    '''

@app.route('/sum')
def sum():
    return str(1 + 2)