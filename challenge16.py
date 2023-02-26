'''Write a function that takes a list 
of words and returns the longest one.'''

def words(words:list):
    longest_word = ''
    for word in words:       
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(words(['ala', 'ana', 'montaña', 'solar']))

