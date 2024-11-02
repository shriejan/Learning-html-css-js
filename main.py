from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
@app.route('/shriejan')
def index2():
    return 'Hello, Shriejan!'
if __name__ == '__main__':
    app.run(debug=True)