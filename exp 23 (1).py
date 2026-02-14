# 23. Text Coherence Evaluation

import math

def sentence_similarity(s1, s2):
    words1 = set(s1.lower().split())
    words2 = set(s2.lower().split())
    common = words1.intersection(words2)
    
    if len(words1) == 0 or len(words2) == 0:
        return 0
    
    return len(common) / math.sqrt(len(words1) * len(words2))


def evaluate_coherence(text):
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]
    
    total_score = 0
    
    for i in range(len(sentences) - 1):
        total_score += sentence_similarity(sentences[i], sentences[i+1])
    
    if len(sentences) > 1:
        return total_score / (len(sentences) - 1)
    else:
        return 0


text = "The cat sits on the mat. The mat is blue. Blue is a color."
print("Coherence Score:", evaluate_coherence(text))
