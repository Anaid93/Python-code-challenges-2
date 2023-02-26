'''Suppose we have more than 3 numbers or we don't know 
how many numbers they are. Write a max_in_list() function 
that takes a list of numbers and returns the largest one.'''

def max_in_list(list_numbers:list):    
    maxi = 0
    for number in list_numbers:
        if number > maxi:
            maxi = number
    return maxi
            
print(max_in_list([3,2,5,8,9,7])) 

