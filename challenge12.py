'''Create a function that receives two arrays, 
a boolean and returns an array.
- If the boolean is true it will search and 
return the common elements of the two arrays.
- If the boolean is false it will search and 
return the non-common elements of the two arrays.'''

def array(array_1:list, array_2:list, booleano):
    intersection = [i for i in array_1 if i in array_2]
    difference_1 = [i for i in array_1 if i not in array_2]
    difference_2 = [i for i in array_2 if i not in array_1]
    difference = difference_1 + difference_2

    if booleano == True:
        return intersection
    elif booleano == False:
        return difference

print(array([2,8,7,9,6,5],[0,1,7,5,3,2], True)) 
print(array([2,8,7,9,6,5],[0,1,7,5,3,2], False)) 
