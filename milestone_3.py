import random

#A functiion that gives a random word from the list of 5 fruits
def choice():
    word = random.choice(["Apple", "Orange", "Banana", "Strawberry", "Mango"])
    return word

word = choice() #this is the randomly chosen word from the list

#The input taken from the user to guess a word
def ask_for_input():
    while True:
        guess = input('Guess a letter : ')
        if (len(guess) == 1 and guess.isalpha()==True):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess(guess):
    if guess in word.lower():
        print(f'Good guess! "{guess}" is in the word.')
    else:
        print(f'Sorry, "{guess}" is not in the word. Try again.')

ask_for_input()