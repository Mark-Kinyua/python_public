import json
from difflib import *

data = json.load(open("/home/mark/programs/python_programs/Dictionary/data.json", "r"))


def translate(x):
    x = x.lower()
    if x in data:
        return data[x]
    elif len(get_close_matches(x, data.keys())) > 0:
        que = input("Did you mean %s instead? Y or N: " % get_close_matches(x, data.keys())[0])
        que = que.lower()
        if que == "y":
            return data[get_close_matches(x, data.keys())[0]]
        elif que == "n":
            return "Sorry for getting the wrong word"
        else:
            return "Wrong input"
    else:
        while len(get_close_matches(x, data.keys())) < 1:
            x = input("The word doesn't exist, kindly input something else: ")
        x = x.lower()
        if x in data:
            return data[x]
        elif len(get_close_matches(x, data.keys())) > 0:
            que = input("Did you mean %s instead? Y or N: " % get_close_matches(x, data.keys())[0])
            que = que.lower()
            if que == "y":
                return data[get_close_matches(x, data.keys())[0]]
            elif que == "n":
                return "Sorry for getting the wrong word"
            else:
                return "Wrong input"


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
