# Starting code courtesy of Carl Anderson
# https://github.com/leapingllamas/p-value.info/blob/master/jokes_2013_01/generate_jokes.py


def indefinite_article(w):
    if w.lower().startswith("a ") or w.lower().startswith("an "):
        return ""
    return "an " if w.lower()[0] in list('aeiou') else "a "


def camel(s):
    return s[0].upper() + s[1:]


# w1 is an adjective and w2 is a noun.
# d1 is an adjective synonym for w1
# d2 is an noun synonym for w2
def N2A2(d1, d2, w1, w2):
    return "What do you call " + indefinite_article(d1) + d1 + " " + d2 + "? " + \
        camel(indefinite_article(w1)) + w1 + " " + w2 + "."


# w1 and w2 are both nouns
# d1 is an noun synonym for w1
# d2 is an noun synonym for w2
def N4(d1, d2, w1, w2):
    return "When is " + indefinite_article(d1) + d1 + " like " + indefinite_article(d2) + d2 + "? " + \
           "When it is " + indefinite_article(w2) + w2 + "."


# w1 is a verb and w2 is a noun
# d1 is an verb synonym for w1
# d2 is an noun synonym for w2
def N2V2(d1, d2, w1, w2):
    return "Why did someone " + d1 + indefinite_article(d2) + d2 + "? " + \
           "So they could " + w1 + indefinite_article(w2) + w2 + "."

# both are nouns, but w1 has a synonym that's an adjective
def N3A(d1, d2, w1, w2):
    return "What do you call " + indefinite_article(d1) + d1 + " " + d2 + "? " + \
           camel(indefinite_article(w2)) + w2 + "."


# adjective with noun synonym is homophones with a noun with a noun synonym
def N2AN(d1, d2, w1, w2):
    return "When is " + indefinite_article(d1) + d1 + " like " + indefinite_article(d2) + d2 + "? " + \
           "When it is " + indefinite_article(w1) + w1 + " " + w2 + "."


# w1 is an adjective and w2 is a noun.
# d1 is the definitions of w1
# d2 is the definitions of w2
def NA(d1, d2, w1, w2):
    defs1 = "|".split(d1)
    defs2 = "|".split(d2)
    defs1.shuffle()
    defs2.shuffle()
    return "What do you call " + indefinite_article(defs1[0]) + defs1[0] + " " + defs2[0] + "? " + \
        camel(indefinite_article(w1)) + w1 + " " + w2 + "."


# w1 and w2 are both nouns
# d1 is the definitions of w1
# d2 is the definitions of w2
def N2(d1, d2, w1, w2):
    defs1 = "|".split(d1)
    defs2 = "|".split(d2)
    defs1.shuffle()
    defs2.shuffle()
    return "When is " + indefinite_article(defs1[0]) + defs1[0] + " like " + indefinite_article(defs2[0]) + defs2[0] + "? " + \
           "When it is " + indefinite_article(w2) + w2 + "."
