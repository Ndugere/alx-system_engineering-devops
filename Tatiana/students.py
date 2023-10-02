with open("students.csv") as file:
    for line in file:
        row = line.strip().split(",")
        print(f"i am {row[0]} from {row[1]}")

