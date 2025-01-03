import random
import string

print("#########################################")
print("#          Password Generator           #")
print("#########################################\n")

try:
    length = int(input("Enter The Length Of Password: "))
    if length < 5:
        print("Password Length Must Be Greater Than 5")
        exit()
except ValueError:
    print("Error Input. Enter a Valid Number")

while True:
    Complexity = input("\nThere are 3 Levels to Complexity of password. Choose one:\n 1) Low \n 2) Medium \n 3) Hard \n\n => ").lower()

    if Complexity == "low":
        mix = string.ascii_lowercase
        break
    elif Complexity == "medium":
        mix = string.ascii_lowercase + string.digits
        break
    elif Complexity == "hard":
        mix = string.ascii_lowercase + string.digits + string.punctuation
        break
    else:
        print("Invalid Complexity")

passwd = ""
for _ in range(length):
    passwd += random.choice(mix)

print(f"\nGenerated Password is: {passwd}")

