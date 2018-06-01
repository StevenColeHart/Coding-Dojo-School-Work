from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def openpage():
    return render_template('/index.html')

@app.route('/ninjas')
def ninjaspage():
    return render_template('/ninjas.html')

@app.route('/dojos/new')
def createninja():
    