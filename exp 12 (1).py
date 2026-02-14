import nltk
from nltk import CFG, EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'dog'
VP -> 'runs'
""")

parser = EarleyChartParser(grammar)

for tree in parser.parse(['dog', 'runs']):
    print(tree)
