import random 
import string


def generate_passsword(min_length,number = True, special_character = True):
    letters = string.ascii_letters   # Making sure we can access all ascii letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    
    if number:
        characters+=digits
    if special_character:
        characters+= special

    pwd = ''

    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length :    
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True 

        if number:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special
    return pwd

min_length = int(input("Enter the Minimum length"))

has_number = input("DO you want to have a numbers (y/n)?").lower() == 'y'
has_speical = input("DO you want to have a speical characters(y/n)").lower() == 'y'

pwd = generate_passsword(min_length,has_number,has_speical)
print("the generated password is ",pwd)
