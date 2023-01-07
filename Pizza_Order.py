# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:55:30 2022

@author: gautam
"""

print("Order your Pizza here....!! ")

print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")


size = input("Which size of Pizza do you want? S, M or L :- ")

if size == "S":
  print("For Small pizza to add pepproni $ = $2.0")
else:
  print("For Large or Medium pizza to add pepproni $ = $3.0")

pepproni = input("Do you want to add pepproni? Y or N :-")

print("To add extra cheese $ = $1.0")

e_cheese = input("Do you want to add extra cheese? Y or N :-")

bill = 0

if size == "S" :
    bill = 15  
    print("Small Pizza is of $15.0")
    if pepproni == "Y":
      bill += 2
      #print("For pepproni extra $ = $2")
    
  
elif size == "M" :
    bill = 20
    print("Medium Pizza is of $20.0")
    
    if pepproni == "Y" :
        bill += 3
        #print("For pepproni extra $ = $3")

   
elif size == "L" :
    bill = 25
    print("Large Pizza is of $25.0")
   
    if pepproni == "Y" :
        bill += 3
        #print("For pepproni extra $ = $3")

   
if e_cheese == "Y" :
    bill += 1
    #print("For extra cheese $ = $1")
    
print(f"Your total bill is ${bill}.0")

print("\n\nThank You..!!")
print("Visit again.")
   
