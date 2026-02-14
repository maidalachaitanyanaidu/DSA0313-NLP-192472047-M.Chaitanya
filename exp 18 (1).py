expr = "likes(John,IceCream)"

pred, args = expr.split("(")
args = args[:-1].split(",")

print("Predicate:", pred)
print("Arguments:", args)
