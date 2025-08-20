
# 3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

para generar numeros aletorios  se utiliza el modulo random hay
 otros modulos utiles para cada situacion siempre se inician usando la palabra import

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Variable to store the user's guess
guess = 0
print("Guess the secret number between 1 and 10!")

# Loop until the user guesses correctly
while guess != secret_number:
    guess = int(input("Your guess: "))
    
    if guess < secret_number:
        print("Too low, try again.")
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print("Correct! You guessed the number.")
