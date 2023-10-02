import csv

name = input("kindly write your name: ")
town = input("kindly write where you come from: ")

with open("data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, town])
