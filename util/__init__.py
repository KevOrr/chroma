import flask

def make_html_resp(payload):
    response = flask.make_response(payload)
    response.headers['content'] = 'text/html; charset=utf-8'
    return response

class _Container(dict):
    def __setattr__(self, name, val):
        self['name'] = val

    def __getattr__(self, name):
        return self['name']

    def __delattr__(self, name):
        self.pop(name)
