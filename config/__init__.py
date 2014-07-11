from util import _Container

__all__ = ['config']

def config(debug=False):
    if debug is True:
        return _DebugConfig()
    else:
        return _ProductionConfig()

class _Config():
    jq_url = 'http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
    d3_url = 'http://d3js.org/d3.v3.min.js'

class _DebugConfig(_Config):
    pass

class _ProductionConfig(_Config):
    pass
