import re

firstNameRegex = re.compile(r'[A-Z][a-z]+')
lastNameRegex = re.compile(r'[A-Z][a-z]+')
emailRegex = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
numberRegex = re.compile(r'\+977 \d{10}')

with open('./credentials.txt', 'w') as file:
    while True:
        firstName = input("Enter your first name: ")
        if firstNameRegex.fullmatch(firstName):
            file.write(f"First Name = {firstName}\n")
            break
        else:
            print('Invalid first name!')

    while True:
        lastName = input("Enter your last name: ")
        if lastNameRegex.fullmatch(lastName):
            file.write(f"Last Name = {lastName}\n")
            break
        else:
            print("Invalid last name!")

    while True:
        email = input("Enter your email address: ")
        if emailRegex.fullmatch(email):
            file.write(f"Email = {email}\n")
            break
        else:
            print("Invalid email address!")

    while True:
        phoneNumber = input("Enter your phone number (e.g. +977 9848397090): ")
        if numberRegex.fullmatch(phoneNumber):
            file.write(f"Phone Number = {phoneNumber}\n")
            break
        else:
            print("Invalid phone number!")

# Read the file content after writing
with open('./credentials.txt', 'r') as fileAgain:
    print("\n--- Saved Credentials ---")
    print(fileAgain.read())
