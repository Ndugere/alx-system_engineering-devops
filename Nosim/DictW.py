import csv

name = input("kindly tell us you name: ")
home = input("kindly tell us your hometown: ")

with open("data.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames= ["Name", "Town"])
    writer.writerow({'Name': name, 'Town': home})
