import random
 
print("Hello, welcome to this game. This is an number guessing game./nYou will get 7 chances to guess the number. Let's start the game.")

number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input("Please enter your guess:"))

    if my_guess == number_to_guess:
        print (f"The number is {number_to_guess} correct !! in the {guess_counter} attempt")
        break
    
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops sorry, The number is {number_to_guess} better luck next time!")

    elif my_guess > number_to_guess:
        print("Your guess is higher")

    elif my_guess < number_to_guess:
        print("Your guess is lower")