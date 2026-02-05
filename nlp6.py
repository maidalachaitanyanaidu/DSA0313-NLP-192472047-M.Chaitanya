import random

text = "i love machine learning and i love python"
words = text.split()

bigrams = {}
for i in range(len(words) - 1):
    key = words[i]
    value = words[i + 1]
    if key not in bigrams:
        bigrams[key] = []
    bigrams[key].append(value)

current_word = "i"
generated = [current_word]

for _ in range(4):
    next_words = bigrams.get(current_word, None)
    if not next_words:
        break
    current_word = random.choice(next_words)
    generated.append(current_word)

print("Generated Text:", " ".join(generated))