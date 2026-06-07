import random

# define range
low = 1
high = 10

# generate random number
secret = random.randint(low, high)

print(f"I have picked a number between {low} and {high}.")

# user input
guess = int(input("Enter your guess: "))

# comparison
if guess == secret:
    print("Correct!")
else:
    print(f"Wrong. The number was {secret}.")