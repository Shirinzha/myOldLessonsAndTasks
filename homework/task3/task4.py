text=input('enter ur text: ')
others = 0
upper_letters = 0
lower_letters = 0
for letter in text:
    if letter.isupper():
        upper_letters+=1
    elif letter.islower():
        lower_letters+=1
    else:
        others+=1    
total = len(text)
print(upper_letters*100//total)            
print(lower_letters*100//total)





