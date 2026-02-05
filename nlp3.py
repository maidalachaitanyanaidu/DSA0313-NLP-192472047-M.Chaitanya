import nltk
from nltk.stem import PorterStemmer

# Input sentence
sentence = "The children are playing happily"

# Tokenization (simple split)
tokens = sentence.split()

# Morphological analysis using stemming
stemmer = PorterStemmer()

print("Word\t\tStem")
print("-----------------------")
for word in tokens:
    print(word, "\t\t", stemmer.stem(word))