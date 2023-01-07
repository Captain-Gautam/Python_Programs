# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:38:58 2022

@author: gautam
"""

print("Let's Play Fizzbuzz Game...!!")

for num in range(1, 101):
    #print(num)
    if num%3 == 0 and num%5 == 0:
        print("fizzbuzz")
    elif num%3 == 0:
        print("Fizz")
        
    elif num%5 == 0:
        print("Buzz")
        
    else:
        print(num)
    
