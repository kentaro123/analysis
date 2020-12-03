# -*- coding: utf-8 -*-
from flask import Flask
import flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('login.html')

@app.route('/result',methods=["POST","GET"])
def look_up():
    client_params = request.form
    return flask.render_template("result.html",cont=client_params['entry1'])

if __name__ == '__main__':
    app.run()