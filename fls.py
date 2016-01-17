#########################################################################
#-*- coding:utf-8 -*-
# File Name: hello_flask.py
#########################################################################
#!/bin/python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    #app.run('0.0.0.0')
    app.run()
