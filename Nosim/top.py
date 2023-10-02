import statistics

Nosim = []

for _ in range (7):
    marks = int(input("amount of marks: "))
    Nosim.append(marks)
ava = statistics.mean(Nosim)
print(f"The avarage marks is {ava}")

