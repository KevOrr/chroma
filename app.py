import sys

import flask
from flask import Flask, render_template, url_for

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
    return make_html_resp(render_template('maps/connector.html',
                        jq_url=c.jq_url, d3_url=c.d3_url))

#############
# REDIRECTS #
#############

@app.route('/index.html')
def _main_redirect_1():
    return flask.redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=debug)
    
