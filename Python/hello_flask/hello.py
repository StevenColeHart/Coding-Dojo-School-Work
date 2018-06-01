from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/success')
def success():
  return render_template('success.html')

@app.route('/index')
def index():
    return render_template('index.html')

app.run(debug=True)