'''Write a function add() and a function multip() 
that add and multiply respectively all the numbers 
in a list. For example: sum([1,2,3,4]) should return 
10 and multip([1,2,3,4]) should return 24.'''

def add(suma:list):
    suma_total = sum(suma)
    return suma_total

print(add([1,2,3,4])) 


from functools import reduce
def multipli(multipli:list):
    multipli_total = reduce(lambda x,y:x*y, multipli)
    return multipli_total

print(multipli([1,2,3,4])) 
