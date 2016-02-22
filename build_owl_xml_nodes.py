import itertools
from definitions import createSyns, wordCollection
import ujson
import sys

POSTable = {"n": "Noun", "v": "Verb", "a": "Adjective"}
objectByLabel = {}

def getWordObj(word):
    label = word.replace(" ", "_")
    wordObj = objectByLabel.get(label, {})
    if label not in objectByLabel:
        wordObj["raw_text"] = word
        wordObj["label"] = label
        wordObj["homophones"] = set()
        wordObj["synonyms"] = []
        wordObj["definition"] = ""
        wordObj["pos"] = ""

        #initialize word obj with synsets
        synset = createSyns(label)
        hypernyms = (h[0] for h in itertools.chain.from_iterable(instance.hypernyms for instance in synset))
        hyponyms = (h[0] for h in itertools.chain.from_iterable(instance.hyponyms for instance in synset))
        if synset:
            wordObj["pos"] = synset[0].pos
            wordObj["definition"] = " | ".join(instance.definition for instance in synset)
            wordObj["synonyms"] = list(set(itertools.chain(hypernyms, hyponyms)))

        #add to our collection
        objectByLabel[label] = wordObj

    return wordObj

with open("homophones.csv", "r") as homoFile:
    for line in homoFile:
        homoGroup = (word.strip() for word in line.split(",") if word.strip())
        homoObjGroup = [getWordObj(homo_word) for homo_word in homoGroup]
        for homoA, homoB in itertools.combinations(homoObjGroup, 2):
            homoA["homophones"].add(homoB["label"])
            homoB["homophones"].add(homoA["label"])

for word, wordObj in objectByLabel.items():
    wordObj["homophones"] = list(wordObj["homophones"])

#dump JSON
with open("puns.json", "w") as outputFile:
    ujson.dump(objectByLabel, outputFile, ensure_ascii=False)

#dump OWL XML here
output ="\n".join(("""
        <!-- http://allyourpunsarebelongto.us/puns.owl#{label} -->

        <owl:NamedIndividual rdf:about="http://allyourpunsarebelongto.us/puns.owl#{label}">
            <rdf:type rdf:resource="http://allyourpunsarebelongto.us/puns.owl#{pos}"/>
            <Definition rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{definition}</Definition>
            <RawText rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{raw_text}</RawText>
        </owl:NamedIndividual>""".format(label=word, pos=POSTable.get(wordObj["pos"], "Word"),
                definition=wordObj["definition"], raw_text=wordObj["raw_text"])
        for word, wordObj in objectByLabel.items()))
print(output)

