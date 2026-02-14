# 24. Dialog Act Recognition

def dialog_act(sentence):
    sentence = sentence.strip()

    if sentence.endswith("?"):
        return "Question"
    elif sentence.lower().startswith(("please", "do", "can you")):
        return "Request"
    elif sentence.endswith("!"):
        return "Exclamation"
    else:
        return "Statement"


conversation = [
    "How are you?",
    "I am fine.",
    "Please help me",
    "Wow!"
]

for line in conversation:
    print(line, "->", dialog_act(line))
