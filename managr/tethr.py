#
# Flask/Werkzeug handler example code
#
# Please note that this is not a complete application, just some example code about how
# to interact with jQuery-File-Upload and how to create the json responses it expects.
#
# (c) 2011 by Thomas Waldmann
# Licensed under MIT license.

import os
import re, cgi

from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
from werkzeug import secure_filename
#from celery import network

UPLOAD_FOLDER = '/var/tethr/files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4', 'wav'])

app = Flask(__name__)
DEBUG = True
SECRET_KEY = 'development key'
app.config.from_object(__name__)

import scripts.network

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
# Jun - Removing extension filtering for now
#
#    return '.' in filename and \
#               filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    return 1

re_string = re.compile(r'(?P<htmlchars>[<&>])|(?P<space>^[ \t]+)|(?P<lineend>\r\n|\r|\n)|(?P<protocal>(^|\s)((http|ftp)://.*?))(\s|$)', re.S|re.M|re.I)
def plaintext2html(text, tabstop=4):
    def do_sub(m):
        c = m.groupdict()
        if c['htmlchars']:
            return cgi.escape(c['htmlchars'])
        if c['lineend']:
            return '<br>'
        elif c['space']:
            t = m.group().replace('\t', '&nbsp;'*tabstop)
            t = t.replace(' ', '&nbsp;')
            return t
        elif c['space'] == '\t':
            return ' '*tabstop;
        else:
            url = m.group('protocal')
            if url.startswith(' '):
                prefix = ' '
                url = url[1:]
            else:
                prefix = ''
            last = m.groups()[-1]
            if last in ['\n', '\r', '\r\n']:
                last = '<br>'
            return '%s<a href="%s">%s</a>%s' % (prefix, url, url, last)
    return re.sub(re_string, do_sub, text)
               
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#            return redirect(url_for('uploaded_file',  filename=filename))
            return redirect('/')
    return redirect('/')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('test'))
    return render_template('login.html', error=error)
    
@app.route('/ifconfig')
def ifconfig():
    return jsonify(result=scripts.network.Command("ifconfig").run().output)

@app.route('/ping')
def ping():
    return jsonify(result=scripts.network.Command("ping 8.8.8.8 -c5").run().output)

@app.route('/route')
def route():
    return jsonify(result=scripts.network.Command("route").run().output)

@app.route('/internet_on')
def internet_on():
    return jsonify(result=scripts.network.internet_on())

@app.route('/pirsyncd_log')
def pirsyncd_log():
    return jsonify(result=scripts.network.Command("tail -n50 /var/log/tethr/.pirsyncd.log").run().output)
@app.route('/managr')
def managr():
    return render_template('managr.html')