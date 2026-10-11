import random

print("Welcome to Number Guessing Game!!!")
print("Guess the Number between 1 to 100")

secret_number = random.randint(1,100)

for i in range(1,8):
    user_input = int(input("Enter the Number:"))
    if user_input < 1 or user_input > 100:
        print("Invalid Number! Please enter the Number between 1-100")
    elif user_input > secret_number:
        print("Your Number Higher!")
    elif user_input < secret_number:
        print("Your Number Lesser!")
    else:
        print("Your Guessed Number is correct Number")
        break

if secret_number == user_input:
    print(f"Congradulations! You have guessed the number {secret_number} in {i} attempts")
else:
    print("Sorry! All your trails is exceeded. Try Again!!")
