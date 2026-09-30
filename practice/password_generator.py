import random

while True:

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    username = input("Enter username: ")

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 8:
                print("Password must be at least 8 characters.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    while True:
        numbers = input("Include numbers? (yes/no): ")

        if numbers.lower() in ["yes", "no"]:
            break

        print("Please answer yes or no only.")

    if numbers.lower() == "yes":
        characters += "0123456789"

    while True:
        symbols = input("Include symbols? (yes/no): ")

        if symbols.lower() in ["yes", "no"]:
            break

        print("Please answer yes or no only.")

    if symbols.lower() == "yes":
        characters += "!@#$%^&*"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print(f"\nGenerating password for {username}")
    print(f"Generated Password: {password}")

    file = open("passwords.txt", "a")
    file.write(f"{username}: {password}\n")
    file.close()

    print(f"Password Length: {len(password)}")
    print("\nPassword generated successfully!")

    while True:
        again = input("\nGenerate another password? (yes/no): ")

        if again.lower() in ["yes", "no"]:
            break

        print("Please answer yes or no only.")

    if again.lower() != "yes":
        break

print("Goodbye!")
