from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/shriejan')
def index2():
    return 'Hello, Shriejan!'
if __name__ == '__main__':
    app.run(debug=True)