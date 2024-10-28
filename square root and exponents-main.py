# Imports go at the top
from microbit import *
import math
a = 9
b = 2
y = 0
z = 0
# Code in a 'while True:' loop repeats forever
while True:
    if button_a.is_pressed():
        y = math.sqrt(a)
        display.show(y)
    if button_b.is_pressed():
        z = b * b
        display.show(z)
