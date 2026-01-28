
secret_number = 7
guess = 0

print("Guess the number between 1 and 10")

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")


#output
Guess the number between 1 and 10
Enter your guess: 5
Too low! Try again.
Enter your guess: 7
🎉 Correct! You guessed the number.
