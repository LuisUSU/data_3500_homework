#Week 7 Programming Activity

import json #imports JSON library
import requests #imports url requests library

url = "https://api.datamuse.com/words?rel_trg=cow" #we set the website we want to request our data from here

req = requests.get(url) #this function requests the information from the url variable

dictionary = json.loads(req.text) #this variable loads the text in the JSON format

for word in dictionary:#We start a FOR LOOP here for our new variable "word" and our range is the totality of the dictionary
    if word["word"] == "cheese":#This is a sub for loop and if the new variable "word" is ever equal to "cheese"
        print("Word: ",word["word"],"|","Score: ", word["score"])
        #then we print the word, which is cheese as we set in our for loop argument, and the "score" key from the dictionary