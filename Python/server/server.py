from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def openpage():
    return render_template('/user.html')

