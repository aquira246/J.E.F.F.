import itertools
from definitions import createSyns, wordCollection
import ujson
import sys

objectByLabel = {}

def getWordObj(word):
    label = word.replace(" ", "_")
    wordObj = objectByLabel.get(label, {})
    if label not in objectByLabel:
        wordObj["raw_text"] = word
        wordObj["label"] = label
        wordObj["homophones"] = []
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
        objectByLabel[word] = wordObj

    return wordObj

with open("homophones.csv", "r") as homoFile:
    for line in homoFile:
        homoGroup = (word.strip() for word in line.split(",") if word.strip())
        homoObjGroup = [getWordObj(homo_word) for homo_word in homoGroup]
        for homoA, homoB in itertools.combinations(homoObjGroup, 2):
            homoA["homophones"].append(homoB["label"])
            homoB["homophones"].append(homoA["label"])

#dump JSON
with open("puns.json", "w") as output:
    ujson.dump(objectByLabel, output, ensure_ascii=False)

#dump OWL XML here

