names = ["Ada","Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ").title()

while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("Name not found")
    print(names)
    name_to_remove = input("Who do you want ego remove? ").title()