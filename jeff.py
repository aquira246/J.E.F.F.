import os, sys
import bottle
from generator import generateN4, generateN2V2, generateNA, generateN2
import random

#initialize our joke cache with jokes
app = bottle.default_app()
app.CACHE_SIZE = 50
app.N4_jokes = generateN4(app.CACHE_SIZE)
app.N2V2_jokes = generateN2V2(app.CACHE_SIZE)
app.NA_jokes = generateNA(app.CACHE_SIZE)
app.N2_jokes = generateN2(app.CACHE_SIZE)

def getJoke():
    """Randomly serve a joke from our cache. Refill a type if it is empty."""
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
        return app.NA_jokes.pop()

    if joke_type == 3:
        if not app.N2_jokes:
            app.N2_jokes = generateN2(app.CACHE_SIZE)
        return app.N2_jokes.pop()

@bottle.route('/')
def index():
    return getJoke()

