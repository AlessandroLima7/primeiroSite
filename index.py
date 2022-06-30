from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def index():
    
    return render_template('first.html')


app.run(host="0.0.0.0", debug=False)
