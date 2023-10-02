name = input("Kindly Write Your 1st Name: ")
with open("data.txt", "a") as file:
    file.write(f"{name}\n")
