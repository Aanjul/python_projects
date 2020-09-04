# For refrence https://github.com/realpython/python-scripts/blob/master/scripts/23_flask_session_test.py

import sys
from flask import Flask, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def set():
   session.clear()
   session['works'] = True
   return redirect(url_for('get'))

@app.route('/get')
def get():
   works = session.get('works', False)
   return str(works)


app.run(sys.argv[1], use_reloader= False)