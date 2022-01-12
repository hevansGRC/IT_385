#!/usr/bin/env python3

# This is a hello user prompt script
# to demonstrate python
# Created by Hunter Evans on 01/12/22

# Set Date
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
current_year = int(year)

# Prompt for user information
user_name = input("What is your name: ")
user_birth_year = int( input("What year were you born: ") )

#Calculate user_age
user_age = int(current_year) - int(user_birth_year)

# Say Hello to user and print their age
print('Hello {0}, you are {1} years old'.format(user_name, user_age)) 

