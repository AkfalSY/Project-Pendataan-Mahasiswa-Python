import random
import string 

def string_random(panjang:int)->str:
    hasil_string = ''.join(random.choice(string.ascii_letters)for i in range(panjang))
    return hasil_string