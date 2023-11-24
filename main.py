#!/usr/bin/env python3

import yaml

from flask import Flask, render_template

app = Flask(__name__)
version = "1.0.0"

@app.route('/')
def home():

    with open('info.yml', 'r') as user:
        info = yaml.full_load(user)

    return render_template('home.html', user=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
