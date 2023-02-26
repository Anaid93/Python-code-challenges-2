'''Write a small program where:
- The current year is entered.
- Enter the name and year of birth of a person.
- Calculate how old she/he will be during the current year.
- It is printed on the screen.'''

def old():
    name = input('Enter your name: ')
    birth = input('Enter the year of your birth: ')
    old = 2023 - int(birth)
    return f'{name}  will be {old} this year'

print(old())
