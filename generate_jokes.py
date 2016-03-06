# Starting code courtesy of Carl Anderson
# https://github.com/leapingllamas/p-value.info/blob/master/jokes_2013_01/generate_jokes.py

import random
import re
import graph_query
from graph_query import query_graph

def indefinite_article(w):
    if (len(w) == 0):
        return ""
    if w.lower().startswith("a ") or w.lower().startswith("an "):
        return ""
    return "an " if w.lower()[0] in list('aeiou') else "a "


def camel(s):
    return s[0].upper() + s[1:]


# w1 is an adjective and w2 is a noun.
# d1 is an adjective synonym for w1
# d2 is an noun synonym for w2
def N2A2_joke(d1, d2, w1, w2):
    return "What do you call " + indefinite_article(d1) + d1 + " " + d2 + "? " + \
        camel(indefinite_article(w1)) + w1 + " " + w2 + "."


# w1 and w2 are both nouns
# d1 is an noun synonym for w1
# d2 is an noun synonym for w2
def N4_joke(d1, d2, w1, w2):
    return "When is " + indefinite_article(d1) + d1 + " like " + indefinite_article(d2) + d2 + "? " + \
           "When it is " + indefinite_article(w2) + w2 + "."


# w1 is a verb and w2 is a noun
# d1 is an verb synonym for w1
# d2 is an noun synonym for w2
def N2V2_joke(d1, d2, w1, w2):
    return "Why did someone " + d2 + " " + indefinite_article(d1) + d1 + "? " + \
           "So they could " + w2 + " " + indefinite_article(w1) + w1 + "."

# both are nouns, but w1 has a synonym that's an adjective
def N3A_joke(d1, d2, w1, w2):
    return "What do you call " + indefinite_article(d1) + d1 + " " + d2 + "? " + \
           camel(indefinite_article(w2)) + w2 + "."


# adjective with noun synonym is homophones with a noun with a noun synonym
def N2AN_joke(d1, d2, w1, w2):
    return "When is " + indefinite_article(d1) + d1 + " like " + indefinite_article(d2) + d2 + "? " + \
           "When it is " + indefinite_article(w1) + w1 + " " + w2 + "."


# w1 is an adjective and w2 is a noun.
# d1 is the definitions of w1
# d2 is the definitions of w2
def NA_joke(d1, d2, w1, w2):
    defs1 = re.split("\s*[;\|]\s*", d1)
    defs2 = re.split("\s*[;\|]\s*", d2)

    if (len(defs1) < 1 or len(defs2) < 1):
        return ""

    random.shuffle(defs1)
    random.shuffle(defs2)
    return "What do you call " + indefinite_article(defs1[0]) + defs1[0] + " " + defs2[0] + "? " + \
        camel(indefinite_article(w1)) + w1 + " " + w2 + "."


# w1 and w2 are both nouns
# d1 is the definitions of w1
# d2 is the definitions of w2
def N2_joke(d1, d2, w1, w2):
    defs1 = re.split("\s*[;\|]\s*", d1)
    defs2 = re.split("\s*[;\|]\s*", d2)

    if (len(defs1) < 1 or len(defs2) < 1):
        return ""

    random.shuffle(defs1)
    random.shuffle(defs2)
    return "When is " + indefinite_article(defs1[0]) + defs1[0] + " like " + indefinite_article(defs2[0]) + defs2[0] + "? " + \
           "When it is " + indefinite_article(w2) + w2 + "."


# generate an array of at most jokeCount N2A2 jokes
def generateN2A2(jokeCount=1):
    jokes = []
    queries = query_graph(graph_query.N2A2, limit=jokeCount, offset=0)
    for q in queries:
        jokes.append(N2A2_joke(q[0], q[1], q[2], q[3]))

    return jokes


# generate an array of at most jokeCount N4 jokes
def generateN4(jokeCount=1):
    jokes = []
    queries = query_graph(graph_query.N4, limit=jokeCount, offset=0)
    for q in queries:
        jokes.append(N4_joke(q[0], q[1], q[2], q[3]))

    return jokes


# generate an array of at most jokeCount N2V2 jokes
def generateN2V2(jokeCount=1):
    jokes = []
    queries = query_graph(graph_query.N2V2, limit=jokeCount, offset=0)
    for q in queries:
        jokes.append(N2V2_joke(q[0], q[1], q[2], q[3]))

    return jokes


# generate an array of at most jokeCount N3A jokes
def generateN3A(jokeCount=1):
    jokes = []
    queries = query_graph(graph_query.N3A, limit=jokeCount, offset=0)
    for q in queries:
        jokes.append(N3A_joke(q[0], q[1], q[2], q[3]))

    return jokes


# generate an array of at most jokeCount N2AN jokes
def generateN2AN(jokeCount=1):
    jokes = []
    queries = query_graph(graph_query.N2AN, limit=jokeCount, offset=0)
    for q in queries:
        jokes.append(N2AN_joke(q[0], q[1], q[2], q[3]))

    return jokes


# generate an array of at most jokeCount N2 jokes
def generateN2(jokeCount=1):
    jokes = []
    queries = query_graph(graph_query.N2, limit=jokeCount, offset=0)
    for q in queries:
        jokes.append(N2_joke(q[1], q[3], q[0], q[2]))

    return jokes


# generate an array of at most jokeCount NA jokes
def generateNA(jokeCount=1):
    jokes = []
    queries = query_graph(graph_query.NA, limit=jokeCount, offset=0)
    for q in queries:
        jokes.append(NA_joke(q[1], q[3], q[0], q[2]))

    return jokes


def randomJoke():
    joke_type = random.randint(0,3)

    if joke_type == 0:
        jokes = generateN4(1)
        if len(jokes) > 0:
            return jokes[0]

    if joke_type == 1:
        jokes = generateN2V2(1)
        if len(jokes) > 0:
            return jokes[0]

    if joke_type == 2:
        jokes = generateNA(1)
        if len(jokes) > 0:
            return jokes[0]

    if joke_type == 3:
        jokes = generateN2(1)
        if len(jokes) > 0:
            return jokes[0]

    joke_type = random.randint(0,4)
    if joke_type == 0:
        return "When is a beef like a club? When it is a meet."
    elif joke_type == 1:
        return "Why did someone slip_in an advertorial? So they could add an ad."
    elif joke_type == 2:
        return "When is a harmonious relations like a serving that has been cut from a larger portion? When it is a piece."
    else:
        return "What do you call a laborer who works in a mine of lesser seriousness or danger? A miner minor."


def generateJokeFile(filename="puns.txt", jokeCount=10):
    wf = open(filename, 'w')

    # get all N2A2 jokes
    wf.writelines("N2A2 Jokes:\n")
    for joke in generateN2A2(jokeCount):
        wf.writelines(joke + "\n")

    # get all N4 jokes
    wf.writelines("N4 Jokes:\n")
    for joke in generateN4(jokeCount):
        wf.writelines(joke + "\n")

    # get all N2V2 jokes
    wf.writelines("N2V2 Jokes:\n")
    for joke in generateN2V2(jokeCount):
        wf.writelines(joke + "\n")

    # get all N3A jokes
    wf.writelines("N3A Jokes:\n")
    for joke in generateN3A(jokeCount):
        wf.writelines(joke + "\n")

    # get all N2AN jokes
    wf.writelines("N2AN Jokes:\n")
    for joke in generateN2AN(jokeCount):
        wf.writelines(joke + "\n")

    # get all NA jokes
    wf.writelines("NA Jokes:\n")
    for joke in generateNA(jokeCount):
        wf.writelines(joke + "\n")

    # get all N2 jokes
    wf.writelines("N2 Jokes:\n")
    for joke in generateN2(jokeCount):
        wf.writelines(joke + "\n")

    wf.close

# generateJokeFile("puns.txt", 20)

for x in range(10):
    print(randomJoke() + "\n")
