with open("data.txt", "r") as file:
    names = file.readlines()
for name in sorted(names):
    print(f"Sasa {name.rstrip()}")
