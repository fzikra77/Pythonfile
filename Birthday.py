# Simple Birthday Storage Program

# Predefined dictionary to store birthdays
birthdays = {
    "Alice": "2000-05-20",
    "Bob": "1995-12-14"
}

print("Welcome to the Birthday Dictionary!")

while True:
    print("\nWhat would you like to do?")
    print("1. Look up a birthday")
    print("2. Add a new birthday")
    print("3. Show all birthdays")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter the name: ")
        if name in birthdays:
            print(f"{name}'s birthday is {birthdays[name]}")
        else:
            print("Sorry, birthday not found.")

    elif choice == "2":
        name = input("Enter the name: ")
        birthday = input("Enter the birthday (YYYY-MM-DD): ")
        birthdays[name] = birthday
        print(f"Birthday for {name} added!")

    elif choice == "3":
        print("\nStored Birthdays:")
        for name in birthdays:
            print(f"{name}: {birthdays[name]}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

