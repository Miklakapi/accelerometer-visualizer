#!/usr/bin/env python

"""This module manages the web server."""
import multiprocessing

from flask import Flask
from multiprocessing import Process

from accelerometer_reader import Accelerometer
from loop_rate import LoopRate

data = multiprocessing.Manager().list()
data.append(0)
data.append(0)
app = Flask(__name__)


def accelerometer(variable):
    try:
        acc = Accelerometer()
        loop = LoopRate(4)
        while True:
            val = acc.run()
            variable[0] = val[0]
            variable[1] = val[1]
            loop.slow_loop()
    except KeyboardInterrupt:
        return


@app.route('/get-data/')
def get_data():
    return {'data': [data[0], data[1]]}


if __name__ == '__main__':
    p = Process(target=accelerometer, args=(data,))
    try:
        p.start()
        app.run('192.168.1.184', debug=True)
    except KeyboardInterrupt:
        p.terminate()
        p.join()
