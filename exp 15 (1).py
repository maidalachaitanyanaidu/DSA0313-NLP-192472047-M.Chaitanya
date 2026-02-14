import nltk
from nltk import PCFG

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'dog' [0.5] | 'cat' [0.5]
VP -> 'runs' [1.0]
""")

parser = nltk.ViterbiParser(grammar)
for tree in parser.parse(['dog', 'runs']):
    print(tree)
