import os, os.path, sys
from urllib.parse import urlparse, urlunsplit

import flask
from flask import Flask, render_template, request, url_for

import config
from util import *

if len(sys.argv) == 2 and sys.argv[1] == 'debug':
    debug = True
else:
    debug = False

production = 'DYNO' in os.environ

if production and debug:
    e = RuntimeError('Cannot run in debug mode in production environment')
    raise e

c = config.config(debug)
app = Flask('__name__')

@app.route('/')
def main():
    return make_html_resp(render_template('index.html',
        production = production, ga_setup_url = c.ga_setup_url))

@app.route('/maps/connector')
def connector_map():
    image_url = get_absolute_url(c.connector_map_image_url)
    return make_html_resp(render_template('maps/connector.html',
        jq_url = c.jq_url, d3_url = c.d3_url, d3_css_url = c.qtip_css_url,
        image_url = image_url, ga_setup_url = c.ga_setup_url,
        debug = debug, production = production))

##########################
# REDIRECTS / REFERENCES #
##########################

@app.route('/index.html')
def _main_redirect_1():
    return flask.redirect(url_for('main'))

@app.route('/favicon.ico')
def icon():
    return app.send_static_file('icons/favicon.ico')

def get_absolute_url(relative):
    host = urlparse(request.url_root)
    return urlunsplit((host.scheme, host.netloc, relative, '', ''))

@app.route('/google43467aa7281da596.html')
def gwebmaster_verification():
    return make_html_resp(app.send_static_file('google43467aa7281da596.html'))

if __name__ == '__main__':
    app.run(debug=debug)
    
