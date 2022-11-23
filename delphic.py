
from random import randrange
import time

def containsNumber(value):
    return any([char.isdigit() for char in value])

def get_random_line(afile, default=" "):
    """Return a random line from the file (or default)."""
    line = default
    for i, aline in enumerate(afile, start=1):
        if randrange(i) == 0:  # random int [0..i)
            line = aline
    if containsNumber(line) == False:
        return line
    else:
        return(" ")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")
print(" A little poem. Generated just for you. ")
print("")
print(" Randomly selected lines from (in their presented order):")
print("")
print(" Poems of Sappho")
print("")
print(" Poems of John Milton")
print("")
print(" Dante's inferno")
print("")
print(" Cut up and presented anew.")
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")
print("            Press the enter key to generate")
print("")
print("")
print("")
print("")



while True:
    try:
        input("")
        
        
        with open('words.txt', encoding='utf-8') as f:
            print(" ", get_random_line(f))
        
        time.sleep(0.03)
        
        with open('milton.txt', encoding='utf-8') as g:
            print(" ", get_random_line(g))
            
        time.sleep(0.03)

        with open('inferno.txt', encoding='utf-8') as h:
            print(" ", get_random_line(h))
            
        time.sleep(0.03)
        
        
    except SyntaxError:
        print("Error. Closing.")
        quit()
            
            
