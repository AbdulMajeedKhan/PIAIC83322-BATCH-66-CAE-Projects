# -*- coding: utf-8 -*-
"""Batch 66 Project 02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j6jTyiDDciEWFbCO9X6HojLDSf5umXwM
"""

# how to work with Python's random module, build functions, work with while loops and conditionals, and get user input.
# Project 2 Guess the Number Game Python Project (computer)
# My Name is: Abdul Majeed
# My Roll Number: PIAIC83322
# My Batch #: 66
# Class evening at SBSA on every saturday

import random

Random_Number=random.randint(1,10)
Guess_Number=0
lives=0

while Guess_Number != Random_Number:
  if lives==3:
    print(f"\n Correct random number is:{Random_Number} \n Now game is over..")
    break
  Guess_Number=int(input("Enter number between 1 to 10:"))
  if Guess_Number>Random_Number:
    print("\nYour enter number is too high, Try again!")
  elif Guess_Number<Random_Number:
    print("\n Your enter number is too low, Try again!")
  else:
    print("\n Congrats, You have guessed the correct number ....... ")
  lives+=1



