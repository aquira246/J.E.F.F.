import os, sys
import bottle
from ..generate_jokes import RandomJoke
import random

CACHE_SIZE = 10
N4_jokes = []
N2V2_jokes = []
NA_jokes = []
N2_jokes = []

def queryJokes():
    if not N4_jokes:
        N4_jokes = generateN4(CACHE_SIZE)
    if not N2V2_jokes:
        N2V2_jokes = generateN2V2(CACHE_SIZE)
    if not NA_jokes:
        NA_jokes = generateNA(CACHE_SIZE)
    if not N2_jokes:
        N2_jokes = generateN2(CACHE_SIZE)

queryJokes()

def getJoke():
    joke_type = random.randint(0,3)
    if joke_type == 0:
        if not N4_jokes:
            N4_jokes = generateN4(CACHE_SIZE)
        return N4_jokes.pop()

    if joke_type == 1:
        if not N2V2_jokes:
            N2V2_jokes = generateN2V2(CACHE_SIZE)
        return N2V2_jokes.pop()

    if joke_type == 2:
        if not NA_jokes:
            NA_jokes = generateNA(CACHE_SIZE)
        return NAjokes.pop()

    if joke_type == 3:
        if not N2_jokes:
            N2_jokes = generateN2(CACHE_SIZE)
        return N2jokes.pop()

@bottle.route('/')
def index():
    return getJoke()

