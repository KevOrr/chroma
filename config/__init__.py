from util import _Container

__all__ = ['config']

def config(debug=False):
    if debug is True:
        return _DebugConfig()
    else:
        return _ProductionConfig()

class _Config():
    connector_map_image_url = '/static/maps/connector.png'
    ga_setup_url = '/static/ga_setup.js'

class _DebugConfig(_Config):
    jq_url = '/static/lib/jquery/jquery-1.11.1.js'
    d3_url = '/static/lib/d3/d3.js'
    qtip_js_url = '/static/lib/qtip/jquery.qtip.js'
    qtip_css_url = '/static/lib/qtip/jquery.qtip.css'

class _ProductionConfig(_Config):
    jq_url = '//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'
    d3_url = '//d3js.org/d3.v3.min.js'
    qtip_js_url = '//cdnjs.cloudflare.com/ajax/libs/qtip2/2.2.0/basic/jquery.qtip.min.js'
    qtip_css_url = '//cdnjs.cloudflare.com/ajax/libs/qtip2/2.2.0/basic/jquery.qtip.min.css'
