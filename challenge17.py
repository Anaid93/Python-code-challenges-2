'''Write a filter_words() function that takes a list 
of words and an integer n, and returns words that 
have more than n characters.'''

def filter_words(list_words:list, integer:int):
    for word in list_words:
        if len(word) > integer:
            print(word) 

filter_words(['ana', 'sol', 'camino', 'luna', 'marino'], 3)