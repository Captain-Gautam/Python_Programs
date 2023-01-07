# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 08:35:45 2022

@author: gautam
"""
input_year = int(input("Enter the Year to be checked: "))
if (input_year%400 == 0):
          print(f"{input_year} is a Leap Year")
elif (input_year%100 == 0):
          print(f"{input_year}is a not the Leap Year")
elif (input_year%4 == 0):
          print(f"{input_year} is a Leap Year")
else:
          print(f"{input_year} is not the Leap Year")
