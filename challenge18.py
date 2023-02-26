'''Write a program that tells the user to enter a string. 
The program has to evaluate the string and tell 
how many uppercase letters it has.'''

#Ana Bolinos has a Black Sphere and her dog Lucas has a Red collar.

def user():
    count = 0
    user = input('Enter a text: ')
    for word in user:
        if word != word.lower():
            count += 1
    print("The text has", count, "capital letters")           

user() 

