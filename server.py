import os
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        pass #TODO

@app.route('/<int:num>', methods = ['GET'])
def vid(num):
    if num > len(os.listdir('/static/video/')):  # the test is finished
        pass #TODO
    else:
        pass #TODO

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
