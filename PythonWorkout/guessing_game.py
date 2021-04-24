import random

def guessing_game():
    magic_num = random.randint(0,101)
    correct_guess = False

    guess = input("Guess a number between 0 and 100: ")
    user_guess = int(guess)

    while(correct_guess == False):

        if(user_guess > magic_num):
            print("Your guess is too high. Ty again.")
            guess = input("New guess: ")
            user_guess = int(guess)
        elif (user_guess < magic_num): 
            print("Your guess is too low. Try again.")
            guess = input("New guess: ")
            user_guess = int(guess)
        else:
            correct_guess = True

    print("Congratulations! You guessed the magic number!")

guessing_game()
