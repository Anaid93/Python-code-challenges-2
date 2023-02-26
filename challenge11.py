'''Create a function that adds 2 numbers 
and returns the result after a few seconds.'''

import time

def add_numbers(num1:int, num2:int, time_sleep):
    time.sleep(time_sleep)
    add = num1 + num2
    return add

print(add_numbers(5,3,5))
