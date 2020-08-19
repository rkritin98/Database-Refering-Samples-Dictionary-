import numpy as np
import pandas as pd 
from difflib import get_close_matches
import json

data = json.load(open("data.json"))

word = input("Type a word and press Enter : ")

def search(word):
    if word in data:
        return(data[word])
    elif word.lower() in data:
        return(data[word.lower()])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif len(get_close_matches(word, data.keys())) >0:
        option=input("Did you mean {}? \n If Yes enter 'y',if not enter any key: ".format(get_close_matches(word,data.keys())[0]))
        if option=='y' or option=='Y':
            return(data[get_close_matches(word,data.keys())[0]])   
        else:
            option=input("Did you mean {}? \n If Yes enter 'y',if not enter any key: ".format(get_close_matches(word,data.keys())[1]))
            if option=='y' or option=='Y':
                return(data[get_close_matches(word,data.keys())[0]])   
            else:
                return("{} not found".format(word))
    else:
        return("{} not found".format(word))

meaning = search(word)

if type(meaning)== list:
    for i in meaning:
        print(i)
        print("\n")
else:
    print(meaning)

