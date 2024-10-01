from flask import Flask, render_template

app = Flask(__name__)

def today(date):
    return date.strfline('%d-%m-%Y')

from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    name = "Diego"
    friends = ["Pablo", "Alex", "Jesus", "Victor"]
    return render_template('index.html', name = name, friends = friends)

@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name = None, age = None):
    if name == None and age == None:
        return 'Hola Mundo'
    elif age == None:
        return f'<h1>Hola, {name}!</h1>'
    else:
        return f'<h1>Hola, {name} el doble de tu edad es {age * 2}!</h1>'

from markupsafe import escape

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'