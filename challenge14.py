'''Define a function superposition() that takes two lists 
and returns True if they have at least 1 member in common or 
returns False otherwise. Write the function using nested loop.'''

def superposition(list_1:list, list_2:list):
    for number in list_1:
        for num in list_2:
            if number == num:
                return True
    return False
            
print(superposition([0,1,2,3], [9,6,7,8,0])) 



