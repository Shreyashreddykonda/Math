# Imports go at the top
from microbit import *
import math
base = 3
height = 4
hyp = 0
h1 = 0
# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        hyp = (base * base) + (height * height)
        h1 = math.sqrt(hyp)
        display.show(h1)
        
        
