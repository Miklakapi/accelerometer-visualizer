#!/usr/bin/env python

"""This module manages the web server."""

from flask import Flask

data = {'x': 0, 'y': 0, 'z': 0}
app = Flask(__name__)


@app.route('/get-data/')
def get_data():
    return {'data': data}


if __name__ == '__main__':
    app.run('192.168.1.3', debug=True)
