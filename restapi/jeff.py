import os, sys
import bottle

@bottle.route('/hello')
def hello():
    return "Hello World!"

