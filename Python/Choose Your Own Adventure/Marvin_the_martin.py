from flask import Flask, render_template,session
app = Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    session['win']=0
    session['fail']=0
    print session['win']
    print session['fail']
    return render_template('homepage.html')
   

@app.route('/choice1')
def choice_1():
    return render_template('choice1.html')

@app.route('/choice2')
def choice_2():
    return render_template('choice2.html')

@app.route('/choice3')
def choice_3():
    return render_template('choice3.html')

@app.route('/victory.html')
def victory():
    return render_template('victory')

@app.route('/fail')
def victory():
    return render_template('fail.html')

app.run(debug=True)
