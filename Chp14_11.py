'''
(Count consonants and vowels) Write a program that prompts the user to enter a
text filename and displays the number of vowels and consonants in the file. Use
a set to store the vowels A, E, I, O, and U.
'''

import sys
import string
from collections import Counter

try:
    file_input = open("Chp14_8 text file.txt", "r")
    text_file = file_input.read()
    vowel_count = {n:sum([1 for char in text_file if char ==n]) for n in 'aeiou'}
    print("The vowel count is: ", vowel_count)
    Consonant_count = {n:sum([1 for char in text_file if char == n]) for n in 'bcdfghjklmnpqrstuvwxyz'}
    print("The consonant count is: ", Consonant_count)
except FileNotFoundError:
    print("text file is not in working directory")
    sys.exit(1)
    file_input.close()
