
# Week 4 - Random Password Generator
# allow the user to choose different lengths (4-300 characters)
# allow the user to select different types of characters (symbols, numbers, lower case, upper case)
# Allow the inclusion of unicode characters ( include instructions on how to type them )
# allow the user to exclude similar characters (such as i, I, l, L, 1, |, and !)
# allow the user to exclude ambiguous characters ( such as {}[]()/\'"!,;:>,. )
# allow the user to ensure the first character is a letter
# allow the user to generate multiple passwords to choose from
# color-code letters, numbers, and symbols for easy identification
#!/usr/bin/env python3
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
    global user_passwd_length
    user_passwd_length = int(input("How many characters in your password human: "))
    if user_passwd_length >= 4 and user_passwd_length <= 300:
        pass

    else:
        print("Please choose a number between 4 and 300 human...")
        passwd_length()

passwd_length()
default_passwd_gen()