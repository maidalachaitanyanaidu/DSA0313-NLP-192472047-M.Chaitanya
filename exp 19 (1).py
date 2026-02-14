# Simple Word Sense Disambiguation without nltk (Lesk-style)

sentence = "He went to the bank to deposit money"
target_word = "bank"

# Predefined senses and definitions
senses = {
    "financial": ["money", "deposit", "loan", "account", "finance"],
    "river": ["river", "water", "shore", "stream"]
}

# Tokenize sentence
words = sentence.lower().split()

best_sense = None
max_overlap = 0

# Lesk-style overlap calculation
for sense, keywords in senses.items():
    overlap = 0
    for word in words:
        if word in keywords:
            overlap += 1

    if overlap > max_overlap:
        max_overlap = overlap
        best_sense = sense

# Output result
print("Sentence:", sentence)
print("Target word:", target_word)

if best_sense == "financial":
    print("Sense: Bank as a financial institution")
elif best_sense == "river":
    print("Sense: Bank of a river")
else:
    print("Sense could not be determined")
