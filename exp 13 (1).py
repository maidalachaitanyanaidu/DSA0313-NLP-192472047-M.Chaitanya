import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'dog'
VP -> 'runs'
""")

parser = nltk.ChartParser(grammar)

trees = list(parser.parse(['dog', 'runs']))

for tree in trees:
    tree.pretty_print()
