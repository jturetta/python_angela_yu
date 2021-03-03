lista = int(input('What\'s the desired range? \n'))
number = 0

for item in range (0,lista):
    if item % 2 == 0:  
        number += item

print(f'The total is {number}.')

