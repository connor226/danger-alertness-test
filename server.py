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
        return redirect(url_for('vid', num = 1, total = len(os.listdir('./static/video/'))))

@app.route('/<int:num>', methods = ['GET', 'POST'])
def vid(num):
    if num > len(os.listdir('./static/video/')):  # the test is finished
        if request.method == 'POST':
            return redirect(url_for('index'))
        if len(record) == num:
            with open('./result.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(record)
        return render_template('end.html')
    else:
        if request.method == 'POST':
            raw_data, new_data = [], 'X'
            if request.form["data"]:
                raw_data = list(request.form["data"].split(','))
                new_data = list(map(float, raw_data))
            if len(new_data) == 1:
                new_data = new_data[0]
            record.append(new_data)
            return redirect(url_for('vid', num = num + 1))
        return render_template('main.html', num = str(num), total = len(os.listdir('./static/video/')))

if __name__ == '__main__':
    app.run(port=8000)
