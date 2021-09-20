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
        if len(record) == num:
            with open('./result.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(record)
        return render_template('end.html')
    else:
        if request.method == 'POST':
            new_data = 'X'
            if request.form["time"]:
                new_data = list(map(lambda x, y, z: f'{x} {y} {z}', map(float, request.form["placeX"].split(',')), map(float, request.form["placeY"].split(',')), map(float,request.form["time"].split(','))))
            record.append(new_data)
            return redirect(url_for('vid', num = num + 1))
        return render_template('main.html', num = str(num), total = len(os.listdir('./static/video/')))

if __name__ == '__main__':
    app.run(port=8000)
