import itertools
from .definitions import createSyns, wordCollection
import ujson
import html
import sys
import nltk

POSTable = {"n": "Noun", "v": "Verb", "a": "Adjective"}
objectByLabel = {}
synonymObjsToAdd = set()

def queueSynonymObjToAdd(word):
    synonymObjsToAdd.add(word)
    return word.replace(" ", "_")

def getWordObj(word):
    """Get the word object for a given word from objectByLabel.
    Create the object if it does not exist and queue its synonyms to be added."""
    label = word.replace(" ", "_")
    wordObj = objectByLabel.get(label, {})
    if label not in objectByLabel:
        #add to our collection
        objectByLabel[label] = wordObj
        wordObj["raw_text"] = word
        wordObj["label"] = label
        wordObj["homophones"] = set()
        wordObj["synonyms"] = []
        wordObj["definition"] = ""
        wordObj["pos"] = ""

        #initialize word obj with synsets
        synset = createSyns(label)
        if synset:
            wordObj["pos"] = synset[0].pos
            wordObj["definition"] = html.escape(" | ".join(instance.definition for instance in synset))
            hypernyms = (h[0] for h in itertools.chain.from_iterable(instance.hypernyms for instance in synset))
            hyponyms = (h[0] for h in itertools.chain.from_iterable(instance.hyponyms for instance in synset))
            wordObj["synonyms"] = list(queueSynonymObjToAdd(synonym)
                                        for synonym in
                                        set(itertools.chain(hypernyms, hyponyms)))
        else:
            #tag the word using nltk if wordnet has no synset
            pos = nltk.pos_tag([word])[0][1]
            if pos.startswith('J'):
                pos = 'a'
            elif pos.startswith('V'):
                pos = 'v'
            elif pos.startswith('N'):
                pos = 'n'
            wordObj["pos"] = pos

    return wordObj

#read in homophones list assuming each line is a group of homophones
with open("homophones.csv", "r") as homoFile:
    for line in homoFile:
        homoGroup = (word.strip() for word in line.split(",") if word.strip())
        homoObjGroup = [getWordObj(homo_word) for homo_word in homoGroup]
        #link each word in the group in pairs
        for homoA, homoB in itertools.combinations(homoObjGroup, 2):
            homoA["homophones"].add(homoB["label"])
            homoB["homophones"].add(homoA["label"])

#add the synonyms that do not have homophones as objs
while len(synonymObjsToAdd):
    getWordObj(synonymObjsToAdd.pop())

#convert our set of homophones to a list
for word, wordObj in objectByLabel.items():
    wordObj["homophones"] = list(wordObj["homophones"])

#dump JSON
with open("puns.json", "w") as outputFile:
    ujson.dump(objectByLabel, outputFile, ensure_ascii=False)

#dump ontology header data
with open("puns-base-top.owl", "r") as baseTopFile:
    print(baseTopFile.read())

#dump OWL XML here
output ="\n".join(("""
        <!-- http://allyourpunsarebelongto.us/puns.owl#{label} -->

        <owl:NamedIndividual rdf:about="http://allyourpunsarebelongto.us/puns.owl#{label}">
            <rdf:type rdf:resource="http://allyourpunsarebelongto.us/puns.owl#{pos}"/>{homophoneRelationships}{synonymRelationships}
            <Definition rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{definition}</Definition>
            <RawText rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{raw_text}</RawText>
        </owl:NamedIndividual>""".format(label=word, pos=POSTable.get(wordObj["pos"], "Word"),
                homophoneRelationships=("".join("""
            <isHomophoneTo rdf:resource="http://allyourpunsarebelongto.us/puns.owl#{homo}"/>""".format(homo=homo)
            for homo in wordObj["homophones"])),
                synonymRelationships=("".join("""
            <isSynonymTo rdf:resource="http://allyourpunsarebelongto.us/puns.owl#{syn}"/>""".format(syn=syn)
            for syn in wordObj["synonyms"])),
                definition=wordObj["definition"], raw_text=wordObj["raw_text"])
        for word, wordObj in objectByLabel.items()))
print(output)

#dump end tag for ontology
with open("puns-base-bottom.owl", "r") as baseBottomFile:
    print(baseBottomFile.read())

