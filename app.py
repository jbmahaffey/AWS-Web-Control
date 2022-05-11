#!/usr/bin/env python3

from urllib import request
from flask import Flask, render_template, request
from sub_modules.instance_info import main
from sub_modules.aws_start import startEC2
from sub_modules.aws_stop import stopEC2
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
app.config['SECRET_KEY'] = '0fae43ab115c0cce5a71f35eb9a8dc3b12d38534e39d5f82'
  
@app.route('/', methods=('GET','POST'))
def index():
    if request.method == 'POST':
        if request.form['task'] == 'start':
            start = startEC2(request.form['akey'], request.form['skey'], request.form['region'])
            return render_template('start.html', status = start)
        elif request.form['task'] == 'stop':
            stop = stopEC2(request.form['akey'], request.form['skey'], request.form['region'])
            return render_template('stop.html', status = stop)
        elif request.form['task'] == 'info':
            info = main(request.form['akey'], request.form['skey'], request.form['region'])
            return render_template('info.html', info = info)
    else:
        return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')
  
# main driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0")