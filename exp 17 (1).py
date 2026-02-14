# Simple WordNet-like dictionary (NO nltk needed)

word = "bank"

wordnet = {
    "bank": [
        "financial institution",
        "side of a river"
    ],
    "apple": [
        "a fruit",
        "a technology company"
    ],
    "bat": [
        "a flying mammal",
        "a sports equipment"
    ]
}

if word in wordnet:
    print("Synsets for word:", word)
    for i, meaning in enumerate(wordnet[word], start=1):
        print(f"{i}. {meaning}")
else:
    print("Word not found")
