import random

def guessing_game():
    magic_num = random.randint(0,101)
    correct_guess = False

    user_guess = input("Guess a number between 0 and 100: ")

    while(correct_guess == False):

        if(user_guess > magic_num):
            print("Your guess is too high. Ty again.")
        elif (user_guess < magic_num): 
            print("Your guess is too low. Try again.")
        else:
            correct_guess = True

    print("Congratulations! You guessed the magic number!")
