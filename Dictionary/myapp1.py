from difflib import get_close_matches
import json
data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y for yes,N for No\n"%get_close_matches(word,data.keys())[0])
        if yn.lower()=='y':
            print(get_close_matches(word,data.keys())[0].upper(),':')
            return data[get_close_matches(word,data.keys())[0]]
        elif yn.lower() == "n":
            return ["The word doesn't exist. Please double check it."]
        else:
            return ["We didn't understand your entry."]
    else:
            return ["The word doesn't exist.Please double check it."]
word = input("Enter word:\t")
result = translate(word)
for ans in result:
    print(ans)
