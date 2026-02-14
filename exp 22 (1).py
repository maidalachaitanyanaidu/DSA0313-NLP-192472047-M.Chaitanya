# 22. Simple Reference Resolution

def reference_resolution(text):
    words = text.split()
    nouns = []
    resolved_text = []

    pronouns = ["he", "she", "it", "they", "him", "her", "them"]

    for word in words:
        clean_word = word.lower().strip(".,")
        
        # Simple noun detection (capitalized word assumed noun)
        if word[0].isupper() and clean_word not in pronouns:
            nouns.append(word)

        if clean_word in pronouns and nouns:
            resolved_text.append(nouns[-1])
        else:
            resolved_text.append(word)

    return " ".join(resolved_text)


text = "Ravi went to school. He met Sita. She was happy."
print(reference_resolution(text))
