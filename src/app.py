#!/usr/bin/env python

"""This module manages the web server."""

import os
import logging
from flask import Flask, send_from_directory, render_template
import multiprocessing
from multiprocessing import Process
from flask_cors import CORS, cross_origin

from accelerometer_reader import Accelerometer
from loop_rate import LoopRate
from measurements_fix import MeasurementsFixer

data = multiprocessing.Manager().list()
data.append(0)
data.append(0)
app = Flask(__name__)
CORS(app)


def accelerometer(variable):
    try:
        acc = Accelerometer()
        loop = LoopRate(30)
        fixer = MeasurementsFixer()
        while True:
            for i in range(3):
                fixer.add_measurement(acc.run())
                loop.slow_loop()
            val = fixer.get_fixed_measurement()
            variable[0] = val[0]
            variable[1] = val[1]
    except KeyboardInterrupt:
        return


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-data/')
def get_data():
    return {'data': [data[0], data[1]]}


if __name__ == '__main__':
    p = Process(target=accelerometer, args=(data,))
    logging.getLogger('werkzeug').disabled = True
    try:
        p.start()
        app.run('192.168.1.185', debug=False)
    except KeyboardInterrupt:
        p.terminate()
        p.join()
