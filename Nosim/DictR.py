import csv

students = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({'Town': row['Town'], 'Name': row['Name']})

def get_name(student):
    return student["Name"]

for student in sorted(students, key=get_name):
    print(f"My names are {student['Name']} and I am from {student['Town']}")
