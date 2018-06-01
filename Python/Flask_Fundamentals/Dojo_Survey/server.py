from flask import Flask, redirect, render_template, request
app= Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/new',methods=['POST'])
def create():
    print "hello"
    name = request.form["your_name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template("new.html", name=name, location=location, comment="comment")

app.run(debug=True)
