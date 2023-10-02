names = []

with open("data.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print("Sasa",name)
