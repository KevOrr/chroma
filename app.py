import os, os.path, sys
from urllib.parse import urlparse, urlunsplit

import flask
from flask import Flask, render_template, request, url_for
import flask.ext.compress

import config
from util import *

debug = 'debug' in sys.argv[1:]
remote_access = 'remote' in sys.argv[1:]
heroku = 'DYNO' in os.environ

if heroku and debug:
    e = RuntimeError('Cannot run in debug mode in production environment')
    raise e

c = config.config(debug)
app = Flask('__name__')
flask.ext.compress.Compress(app)


@app.route('/index.html')
@app.route('/')
def main():
    return make_html_resp(render_template('index.html',
        heroku = heroku, ga_setup_url = c.ga_setup_url))

@app.route('/maps/connector')
def connector_map():
    image_url = get_absolute_url(c.connector_map_image_url)
    return make_html_resp(render_template('maps/s2/connector.html',
        jq_url = c.jq_url, d3_url = c.d3_url, d3_css_url = c.qtip_css_url,
        image_url = image_url, ga_setup_url = c.ga_setup_url,
        debug = debug, heroku = heroku))

##########################
# REDIRECTS / REFERENCES #
##########################

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('icons/favicon.ico')

def get_absolute_url(relative):
    host = urlparse(request.url_root)
    return urlunsplit((host.scheme, host.netloc, relative, '', ''))

@app.route('/google43467aa7281da596.html')
def gwebmaster_verification():
    return make_html_resp(app.send_static_file('google43467aa7281da596.html'))

if __name__ == '__main__':
    if debug:
        app.run('127.0.0.1', debug=True)
    else:
        app.run('0.0.0.0', debug=False)
    
