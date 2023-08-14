import random 

word_list = ["Apple", "Orange", "Banana", "Strawberry", "Mango"]
print(word_list)

def choice(list_to_choose_item_from):
    word = random.choice(list_to_choose_item_from)
    print(word)
    return word

def guess_checker(single_letter_check): 
    if (len(single_letter_check) == 1 and single_letter_check.isalpha()==True):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

word = choice(word_list)

guess = guess_checker(input("Enter a single letter : "))