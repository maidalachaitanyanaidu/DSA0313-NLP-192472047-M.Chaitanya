words = ["dogs", "run"]
tags = ["NN", "NN"]

if words[0].endswith("s"):
    tags[0] = "NNS"
if words[1] == "run":
    tags[1] = "VB"

print(list(zip(words, tags)))
