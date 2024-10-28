# Imports go at the top
from microbit import *
e = []
import random
import speech
v1 = 0

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        v1 = random.randint(1, 10)
        e.append(v1)
    if button_b.was_pressed:
        z = len(e)
        for i in range(0, z, 1):
            p = e[i]
            p1 = str(p)
            speech.say(p1)
            sleep(1000)
        
            
        
        
