import json
from difflib import get_close_matches

data = json.load(open(r"C:\Users\Acer\Desktop\Python more\udemy\mega course\app5 desktop app\dictionary app\data.json"))

#print(data)

def translate(w):
    flag=False #u can also take left(dialouge box) or right(dialouge box) and return this value also(see below)
    w = w.lower()
    if w in data:
        return data[w], flag #return left or right here also. In fron end pass left or right acc to ur requirement
    elif w.title() in data:
        return data[w.title()], flag
    elif w.upper() in data:
        return data[w.upper()], flag
    elif len(get_close_matches(w, data.keys(), n=5, cutoff=0.6))>0:
        flag = True 
        return get_close_matches(w, data.keys()), flag
        '''yn = input("Did you mean %s insted? Press Y if Yes or N if No: " % get_close_matches(w, data.keys())[0])
        if yn == Y:
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == N:
            return "The word does not exist. Plese double check it."
        else:
            return "We did not understand your query. "'''
    else:
        return "Word does not exits. Please double check the data. ", flag
#word = input("Enter the word you want to search: ")

'''output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)'''
