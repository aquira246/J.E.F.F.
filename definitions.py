import nltk
from nltk.corpus import wordnet as wn

class wordCollection(object):
    """docstring for wordCollection"""

    def __init__(self, word, pos, hypernyms, hyponyms, definition):
        super(wordCollection, self).__init__()
        self.word = word
        self.pos = pos
        self.hypernyms = hypernyms      #(word, pos)
        self.hyponyms = hyponyms        #(word, pos)
        self.definition = definition


def printSyns(syns):
    for s in syns:
        print("word: ", s.word)

        print("hypernyms: ")
        for (n, p) in s.hypernyms:
            print ("   ", n, "  ", p)

        print("hyponyms: ")
        for (n, p) in s.hyponyms:
            print ("   ", n, "  ", p)

        print("definition: ", s.definition)

        print("pos: ", s.pos)
        print("\n")


def createSyns(word):
    ret = []
    # i = 0
    for syn in wn.synsets(word):
        # if (i == 0):
        #     print(dir(syn), "\n")
        #     i += 1

        name = syn.name().split(".")[0]
        if word in name:
            hypernyms = []
            for h in syn.hypernyms():
                h_name = h.name().split(".")
                hypernyms.append( (h_name[0], h_name[1]) )

            hyponyms = []
            for h in syn.hyponyms():
                h_name = h.name().split(".")
                hyponyms.append( (h_name[0], h_name[1]) )

            ret.append(wordCollection(name, syn.pos(), hypernyms, hyponyms, syn.definition()))

    return ret

#printSyns(createSyns("cheese"))
# createSyns("dog")
#printSyns(createSyns("rock"))
