import rdflib
import os
import pickle
import sys

GRAPH_PICKLE_PATH = "puns.p"
#graph
g = None

try:
    with open(GRAPH_PICKLE_PATH, "rb") as graph_pickle:
        g = pickle.load(graph_pickle)
except IOError:
    g = rdflib.Graph()
    g.load("puns.owl")
    with open(GRAPH_PICKLE_PATH, "wb") as out:
        pickle.dump(g, out)

if not g:
    print("Error loading graph")
    sys.exit(-1)

print("graph has %s statements." % len(g))
# prints graph has 79 statements.

query="""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX puns: <http://allyourpunsarebelongto.us/puns.owl#>

    SELECT ?w1 ?d1 ?w2 ?d2 ?w3 ?d3 ?w4 ?d4
    WHERE {
        ?s1 rdf:type ?t1.
        {?t1 rdfs:subClassOf* puns:Adjective} UNION {?t1 rdfs:subClassOf* puns:Verb}.
        ?s2 rdf:type ?t2. ?t2 rdfs:subClassOf* puns:Noun.
        ?s3 rdf:type ?t3.
        {?t3 rdfs:subClassOf* puns:Adjective} UNION {?t3 rdfs:subClassOf* puns:Verb}.
        ?s4 rdf:type ?t4. ?t4 rdfs:subClassOf* puns:Noun.

        ?s1 puns:isSynonymTo ?s3.
        ?s2 puns:isSynonymTo ?s4.
        ?s3 puns:isHomophoneTo ?s4.

        ?s1 puns:RawText ?w1.
        ?s2 puns:RawText ?w2.
        ?s3 puns:RawText ?w3.
        ?s4 puns:RawText ?w4.

        ?s1 puns:Definition ?d1.
        ?s2 puns:Definition ?d2.
        ?s3 puns:Definition ?d3.
        ?s4 puns:Definition ?d4.
    }
    LIMIT 10
"""

for row in g.query(query):
    w1,d1,w2,d2,w3,d3,w4,d4 = row
    print("What do you call a %s %s?\nA %s %s!"
        % (w1.toPython(), w2.toPython(), w3.toPython(), w4.toPython()))

