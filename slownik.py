#text="this is a simple simple very simple word"
#print(text.split())
from string import punctuation
from collections import defaultdict

def words_count(text:str)->dict:
    slownik={}
    text = text.lower()
    for char in punctuation:
        text = text.replace(char, "")
    words = text.split()

    for word in words:
        if word in slownik:
            slownik[word]+=1
        else:
            slownik[word]=1
    return slownik

print(words_count("this is a simple* Simple. Simple very simple word"))


