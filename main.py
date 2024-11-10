from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Shriejan'
    lst= ["blue", "red", "yellow", "green", "orange"]
    name_age={"shriejan": 21,"Ali": 7.9, "umair": 10, "shruti": 5}


    return render_template('index.html',name = name,colors = lst,name_age = name_age)




@app.route('/shriejan')
def index2():
    return 'Hello, Shriejan!'



if __name__ == '__main__':
    app.run(debug=True)