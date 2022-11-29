import sys
import time
import os
'''
enter the text u want

'''
text = input('Enter a text : ')


def typewriter(text):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


os.system('clear')

typewriter(text)