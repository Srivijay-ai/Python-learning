print("Welcome to Number Guessing Game!!!")
print("Guess the Number between 1 to 100")

secret_number = 75

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
        print(f"Congradulations! You have guessed the number {secret_number} in {i} attempts")
        break
