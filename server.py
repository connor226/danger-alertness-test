import os
import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
record = []

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        record.clear()
        return render_template('index.html')
    elif request.method == 'POST':
        record.append(request.form['test-id'])
        return redirect(url_for('vid', num = 1))

@app.route('/<int:num>', methods = ['GET', 'POST'])
def vid(num):
    if num > len(os.listdir('./static/video/')):  # the test is finished
        if request.method == 'POST':
            return redirect(url_for('index'))
        with open('./result.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(record)
        return render_template('end.html')
    else:
        if request.method == 'POST':
            raw_data, new_data = [], 'X'
            if request.form["data"]:
                raw_data = list(request.form["data"].split(','))
            if len(raw_data):
                new_data = list(map(float, raw_data))
            record.append(new_data)
            return redirect(url_for('vid', num = num + 1))
        return render_template('main.html', num = str(num))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
