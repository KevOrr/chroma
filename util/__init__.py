import flask

all = ['make_html_resp']

def make_html_resp(payload):
    response = flask.make_response(payload)
    response.headers['content'] = 'text/html; charset=utf-8'
    return response
