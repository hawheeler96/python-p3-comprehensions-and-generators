#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers
print(return_evens([0,1,2,3,4,5,6,7,8,9,10]))


def make_exclamation(sentence_list):
    exclamations = [f"{phrase}!" for phrase in sentence_list]
    return exclamations
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))