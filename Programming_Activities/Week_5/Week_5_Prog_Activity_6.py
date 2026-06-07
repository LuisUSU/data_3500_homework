#Week 5 Programming Activity 6
snt = "dude, I just biked down that mountain and at first I was like Whoa and then I was like Whoa"
print(snt)
snt = snt.capitalize()

splitSnt = snt.split(" ")

whoa1 = True

i = 0
for word in words:
    if words[i] == "whoa" and whoa1:
        words[i] = words[i].lower()
        whoa1 = False
    elif words[i] == "whoa" and not whoa1:
        words[i] = words[i].upper()
    else:
        pass
    i += 1

new_sentence = ""
for word in words:
    newStn +=" " + word

print(newStn)
