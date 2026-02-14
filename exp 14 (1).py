def check(sentence):
    if sentence == ["dogs", "run"]:
        return "Agreement Correct"
    elif sentence == ["dogs", "runs"]:
        return "Agreement Incorrect"
    else:
        return "Unknown Sentence"

print(check(["dogs", "run"]))
print(check(["dogs", "runs"]))
