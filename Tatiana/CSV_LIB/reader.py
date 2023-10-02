import csv

students = []

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "town": row[1]})

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"I am {student['name']} from {student['town']}")
