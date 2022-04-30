import random
from tokenize import Number

'''
random number generator from 1 to 90, excludes the number if it has been chosen.
'''
class Generator:
    
    @staticmethod
    def generate_number(number):
        list_generate = []
        while len(list_generate) != number:
            number_random = random.randrange(1, 91)
            if number_random not in list_generate:
               list_generate.append(number_random)
        number = [n for n in list_generate]
        return number 
         
    
         