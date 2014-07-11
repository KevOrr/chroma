import os.path, sys
from urllib.parse import urlparse, urlunsplit

import flask
from flask import Flask, render_template, request, url_for

import config
from util import *

if len(sys.argv) == 2 and sys.argv[1] == 'debug':
    debug = True
else:
    debug = False

c = config.config(debug)
app = Flask('__name__')

@app.route('/')
def main():
    return app.send_static_file('index.html')

@app.route('/maps/connector')
def connector_map():
    image_url = get_absolute_url(c.connector_map_image_url)
    return make_html_resp(render_template('maps/connector.html',
                        jq_url=c.jq_url, d3_url=c.d3_url,
                        image_url = image_url))

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

if __name__ == '__main__':
    app.run(debug=debug)
    
