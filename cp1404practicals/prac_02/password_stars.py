
MINIMUM = 10
password = input("Enter password: ")
while password < MINIMUM:
    print()
    password = input("Enter password: ")

for i in range(0, len(password)):
    print("*", end="")