import sys

with open("data.txt") as file:
    for line in file:
        if line == "David":
            print("found the chosen one")
            sys.exit()
    print("He is not in the list")

