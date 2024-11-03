from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Shriejan'
    return render_template('index.html',name = name)
@app.route('/shriejan')
def index2():
    return 'Hello, Shriejan!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)