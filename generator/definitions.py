import nltk
from nltk.corpus import wordnet as wn

class wordCollection(object):
    """a collection of possible joke material for a word"""

    def __init__(self, word, pos, hypernyms, hyponyms, definition):
        super(wordCollection, self).__init__()
        self.word = word
        self.pos = pos
        self.hypernyms = hypernyms      #(word, pos)
        self.hyponyms = hyponyms        #(word, pos)
        self.definition = definition


# takes in a synset and prints out the word, hypernyms, hyponyms, pos, and
# definition for each word in the synset
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


# create a collection of wordcollections for a passed in word
def createSyns(word):
    ret = []

    # go through each synonym in the synset
    for syn in wn.synsets(word):

        # store the name
        name = syn.name().split(".")[0]

        # filter out strange synonyms
        if word in name:

            # collect the hypernyms
            hypernyms = []
            for h in syn.hypernyms():
                h_name = h.name().split(".")
                hypernyms.append( (h_name[0].strip(), h_name[1].strip()) )

            # collect the hyponyms
            hyponyms = []
            for h in syn.hyponyms():
                h_name = h.name().split(".")
                hyponyms.append( (h_name[0].strip(), h_name[1].strip()) )

            ret.append(wordCollection(name, syn.pos(), hypernyms, hyponyms, syn.definition()))

    # return the collection of wordcollections
    return ret
