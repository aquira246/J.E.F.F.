import os, sys
import bottle
from generator import generateN4, generateN2V2, generateNA, generateN2
import random

app = bottle.default_app()
app.CACHE_SIZE = 10
app.N4_jokes = []
app.N2V2_jokes = []
app.NA_jokes = []
app.N2_jokes = []

def queryJokes():
    app = bottle.default_app()
    if not app.N4_jokes:
        app.N4_jokes = generateN4(app.CACHE_SIZE)
    if not app.N2V2_jokes:
        app.N2V2_jokes = generateN2V2(app.CACHE_SIZE)
    if not app.NA_jokes:
        app.NA_jokes = generateNA(app.CACHE_SIZE)
    if not app.N2_jokes:
        app.N2_jokes = generateN2(app.CACHE_SIZE)

queryJokes()

def getJoke():
    app = bottle.default_app()
    joke_type = random.randint(0,3)
    if joke_type == 0:
        if not app.N4_jokes:
            app.N4_jokes = generateN4(app.CACHE_SIZE)
        return app.N4_jokes.pop()

    if joke_type == 1:
        if not app.N2V2_jokes:
            app.N2V2_jokes = generateN2V2(app.CACHE_SIZE)
        return app.N2V2_jokes.pop()

    if joke_type == 2:
        if not app.NA_jokes:
            app.NA_jokes = generateNA(app.CACHE_SIZE)
        return NA_jokes.pop()

    if joke_type == 3:
        if not app.N2_jokes:
            app.N2_jokes = generateN2(app.CACHE_SIZE)
        return N2_jokes.pop()

@bottle.route('/')
def index():
    return getJoke()

