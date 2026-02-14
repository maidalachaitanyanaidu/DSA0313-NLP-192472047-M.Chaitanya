# Tokenization without NLTK (Pure Python)

sentence = "Natural Language Processing is interesting."

# Convert to lowercase
sentence = sentence.lower()

# Remove punctuation
punctuation = ".,!?;:"
for p in punctuation:
    sentence = sentence.replace(p, "")

# Tokenization
tokens = sentence.split()

# Output
print("Sentence:", sentence)
print("Tokens:")
for token in tokens:
    print(token)
