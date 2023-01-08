# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:32:06 2022

@author: gautam
"""

#num =str(len(input("What is your name?")))
#print("Your name has " + num + " characters")
 
s = int(input("Enter a two digit number:-"))    

#print(type(s))
fd = s/10

ld = s%10

sum = int(fd + ld)

print("The sum of two digit number is",sum)              

#Another Method to sum of fd & ld

# =============================================================================
# n = input("Enter two digit number:-")
# 
# fd = int(n[0])
# ld = int(n[1])
# 
# sum = fd+ld
# 
# print("Your sum is" ,sum)
# 
# =============================================================================
