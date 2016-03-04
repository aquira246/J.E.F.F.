import rdflib
import pickle

g = rdflib.Graph()
g.load("puns.owl")

with open("puns.p", "wb") as out:
   pickle.dump(g, out)

