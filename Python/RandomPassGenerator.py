#!/usr/bin/env python3
# Week 4 - Random Password Generator
# allow the user to choose different lengths (4-300 characters)
# allow the user to select different types of characters (symbols, numbers, lower case, upper case)
# Allow the inclusion of unicode characters ( include instructions on how to type them )
# allow the user to exclude similar characters (such as i, I, l, L, 1, |, and !)
# allow the user to exclude ambiguous characters ( such as {}[]()/\'"!,;:>,. )
# allow the user to ensure the first character is a letter
# allow the user to generate multiple passwords to choose from
# color-code letters, numbers, and symbols for easy identification

# Import modules
import string
import secrets

# Set passwd var
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
default_passwd_var = lower_case + upper_case + num + symbols

# Default passwd function
def default_passwd_gen():
    passwd = ''.join(secrets.choice(default_passwd_var) for i in range(user_passwd_length)) 
    print("Human, I present your password: {0}".format(passwd))
    raise SystemExit

# Input passwd length function
def passwd_length():
    passwd_length = int(input("How many characters in your password human: "))
    return passwd_length

# Input default or user defined settings
def default_passwd():
    user_setting = input("Would you like to use the default character settings (yes/no): ")
    if user_setting == "yes":
        default_passwd_gen()
    elif user_setting == "no":
        pass
    else:
        print("Please type either 'yes' or 'no'")
        default_passwd()

# Input desired character var
#def choose_symbols():
    user_choice = input("Would you like to use symbols and punctuation (yes/no): ")
    if user_choice == "yes":
        user_symbols = string.punctuation
        return user_symbols
    elif user_choice == "no":
        pass
    else:
        print("Please type either 'yes' or 'no'")
        choose_symbols()

#def choose_numbers():
    user_choice = input("Would you like to use numbers (yes/no): ")
    if user_choice == "yes":
        user_num = string.digits
        return user_num
    elif user_choice == "no":
        pass 
    else:
        print("Please type either 'yes' or 'no'")
        choose_numbers()

#def choose_uppercase():
    user_choice = input("Would you like to use upper case letters (yes/no): ")
    if user_choice == "yes":
        user_uppercase = string.ascii_uppercase
        return user_uppercase
    elif user_choice == "no":
        pass
    else:
        print("Please type either 'yes' or 'no'")
        choose_uppercase()

#def choose_lowercase():
    user_choice = input("Would you like to use lower case case letters (yes/no): ")
    if user_choice == "yes":
        user_lowercase = string.ascii_lowercase
        return user_lowercase
    elif user_choice == "no":
        pass
    else:
        print("Please type either 'yes' or 'no'")
        choose_lowercase()

# Set passwd variables
user_passwd_length = passwd_length()
default_passwd()
user_symbols = choose_symbols()
user_num = choose_numbers()
user_uppercase = choose_uppercase()
user_lowercase = choose_lowercase()
#user_passwd_var = add_user_var()

#user_settings = var_set.translate({ord('):None})
# Generate user_passwd function
def user_passwd_gen():
    passwd = ''.join(secrets.choice(user_passwd_var) for i in range(user_passwd_length))
    print("Human, I present your password: {0}".format(passwd))
    raise SystemExit
user_passwd_gen()