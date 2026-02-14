# TF-IDF implementation without sklearn (Pure Python)

import math

documents = [
    "I love NLP",
    "I love Python",
    "NLP and Python are useful"
]

# Step 1: Tokenization
docs_tokens = [doc.lower().split() for doc in documents]

# Step 2: Vocabulary
vocab = sorted(set(word for doc in docs_tokens for word in doc))

# Step 3: Term Frequency (TF) - normalized
tf = []
for doc in docs_tokens:
    doc_tf = {}
    total_words = len(doc)
    for word in vocab:
        doc_tf[word] = doc.count(word) / total_words
    tf.append(doc_tf)

# Step 4: Inverse Document Frequency (IDF)
N = len(documents)
idf = {}

for word in vocab:
    df = sum(1 for doc in docs_tokens if word in doc)
    idf[word] = math.log(N / df)

# Step 5: TF-IDF
tf_idf = []
for doc_tf in tf:
    doc_tfidf = {}
    for word in vocab:
        doc_tfidf[word] = doc_tf[word] * idf[word]
    tf_idf.append(doc_tfidf)

# Step 6: Display Result
for i, doc in enumerate(tf_idf, start=1):
    print("\nDocument", i, "TF-IDF values:")
    for word in vocab:
        print(word, ":", round(doc[word], 3))
