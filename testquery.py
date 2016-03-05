import rdflib
import os
import pickle
import sys
import re

GRAPH_OWL_PATH = "puns.owl"
GRAPH_PICKLE_PATH = "puns.p"

QUERY_PREFIX="""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX puns: <http://allyourpunsarebelongto.us/puns.owl#>
"""

#graph
g = None

try:
    with open(GRAPH_PICKLE_PATH, "rb") as graph_pickle:
        g = pickle.load(graph_pickle)
except IOError:
    g = rdflib.Graph()
    g.load(GRAPH_OWL_PATH)
    with open(GRAPH_PICKLE_PATH, "wb") as out:
        pickle.dump(g, out)

if not g:
    print("Error loading graph")
    sys.exit(-1)

print("graph has %s statements." % len(g))
# prints graph has 79 statements.

N2 = QUERY_PREFIX + """
    SELECT ?w1 ?d1 ?w2 ?d2
    WHERE {
        ?s1 rdf:type ?t1. ?t1 rdfs:subClassOf* puns:Noun.
        ?s2 rdf:type ?t2. ?t2 rdfs:subClassOf* puns:Noun.

        ?s1 puns:isHomophoneTo ?s2.

        ?s1 puns:RawText ?w1.
        ?s2 puns:RawText ?w2.

        ?s1 puns:Definition ?d1.
        ?s2 puns:Definition ?d2.
    }
    LIMIT 10
    OFFSET %d
"""

NA = QUERY_PREFIX + """
    SELECT ?w1 ?d1 ?w2 ?d2
    WHERE {
        ?s1 rdf:type ?t1. ?t1 rdfs:subClassOf* puns:Noun.
        ?s2 rdf:type ?t2. ?t2 rdfs:subClassOf* puns:Adjective.

        ?s1 puns:isHomophoneTo ?s2.

        ?s1 puns:RawText ?w1.
        ?s2 puns:RawText ?w2.

        ?s1 puns:Definition ?d1.
        ?s2 puns:Definition ?d2.
    }
    LIMIT 10
    OFFSET %d
"""

N2A2 = QUERY_PREFIX + """
    SELECT ?w1 ?w2 ?w3 ?w4
    WHERE {
        ?s1 rdf:type ?t1. ?t1 rdfs:subClassOf* puns:Noun.
        ?s2 rdf:type ?t2. ?t2 rdfs:subClassOf* puns:Adjective.
        ?s3 rdf:type ?t3. ?t3 rdfs:subClassOf* puns:Noun.
        ?s4 rdf:type ?t4. ?t4 rdfs:subClassOf* puns:Adjective.

        ?s1 puns:isSynonymTo ?s3.
        ?s2 puns:isSynonymTo ?s4.
        ?s3 puns:isHomophoneTo ?s4.

        ?s1 puns:RawText ?w1.
        ?s2 puns:RawText ?w2.
        ?s3 puns:RawText ?w3.
        ?s4 puns:RawText ?w4.
    }
    LIMIT 10
    OFFSET %d
"""

N2AN = QUERY_PREFIX + """
    SELECT ?w1 ?w2 ?w3 ?w4
    WHERE {
        ?s1 rdf:type ?t1. ?t1 rdfs:subClassOf* puns:Noun.
        ?s2 rdf:type ?t2. ?t2 rdfs:subClassOf* puns:Noun.
        ?s3 rdf:type ?t3. ?t3 rdfs:subClassOf* puns:Noun.
        ?s4 rdf:type ?t4. ?t4 rdfs:subClassOf* puns:Adjective.

        ?s1 puns:isSynonymTo ?s3.
        ?s2 puns:isSynonymTo ?s4.
        ?s3 puns:isHomophoneTo ?s4.

        ?s1 puns:RawText ?w1.
        ?s2 puns:RawText ?w2.
        ?s3 puns:RawText ?w3.
        ?s4 puns:RawText ?w4.
    }
    LIMIT 10
    OFFSET %d
"""

N2V2 = QUERY_PREFIX + """
    SELECT ?w1 ?w2 ?w3 ?w4
    WHERE {
        ?s1 rdf:type ?t1. ?t1 rdfs:subClassOf* puns:Noun.
        ?s2 rdf:type ?t2. ?t2 rdfs:subClassOf* puns:Verb.
        ?s3 rdf:type ?t3. ?t3 rdfs:subClassOf* puns:Noun.
        ?s4 rdf:type ?t4. ?t4 rdfs:subClassOf* puns:Verb.

        ?s1 puns:isSynonymTo ?s3.
        ?s2 puns:isSynonymTo ?s4.
        ?s3 puns:isHomophoneTo ?s4.

        ?s1 puns:RawText ?w1.
        ?s2 puns:RawText ?w2.
        ?s3 puns:RawText ?w3.
        ?s4 puns:RawText ?w4.
    }
    LIMIT 10
    OFFSET %d
"""

N3A = QUERY_PREFIX + """
    SELECT ?w1 ?w2 ?w3 ?w4
    WHERE {
        ?s1 rdf:type ?t1. ?t1 rdfs:subClassOf* puns:Noun.
        ?s2 rdf:type ?t2. ?t2 rdfs:subClassOf* puns:Adjective.
        ?s3 rdf:type ?t3. ?t3 rdfs:subClassOf* puns:Noun.
        ?s4 rdf:type ?t4. ?t4 rdfs:subClassOf* puns:Noun.

        ?s1 puns:isSynonymTo ?s3.
        ?s2 puns:isSynonymTo ?s4.
        ?s3 puns:isHomophoneTo ?s4.

        ?s1 puns:RawText ?w1.
        ?s2 puns:RawText ?w2.
        ?s3 puns:RawText ?w3.
        ?s4 puns:RawText ?w4.
    }
    LIMIT 10
    OFFSET %d
"""

N4 = QUERY_PREFIX + """
    SELECT ?w1 ?w2 ?w3 ?w4
    WHERE {
        ?s1 rdf:type ?t1. ?t1 rdfs:subClassOf* puns:Noun.
        ?s2 rdf:type ?t2. ?t2 rdfs:subClassOf* puns:Noun.
        ?s3 rdf:type ?t3. ?t3 rdfs:subClassOf* puns:Noun.
        ?s4 rdf:type ?t4. ?t4 rdfs:subClassOf* puns:Noun.

        ?s1 puns:isSynonymTo ?s3.
        ?s2 puns:isSynonymTo ?s4.
        ?s3 puns:isHomophoneTo ?s4.

        ?s1 puns:RawText ?w1.
        ?s2 puns:RawText ?w2.
        ?s3 puns:RawText ?w3.
        ?s4 puns:RawText ?w4.
    }
    LIMIT 10
    OFFSET %d
"""

#use re.split("\s*[;\|]\s*", x) for splitting definitions
#old test code
"""
for row in g.query(N4query % offset):
    w1,d1,w2,d2,w3,d3,w4,d4 = tuple(x.toPython() for x in row)
    d1,d2,d3,d4 = tuple(re.split("\s*[;\|]\s*", x) for x in (d1,d2,d3,d4))

    joke1.append("What do you call a %s %s?\nA %s %s!" % (w1, w2, w3, w4))
"""

def query_graph(query_string, offset=0):
    return g.query(query_string % offset)

