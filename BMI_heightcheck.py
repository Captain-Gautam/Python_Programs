# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:37:46 2022

@author: gautam
"""
print("BMI with Suitable name weight..")

wg = float(input("Enter the weight in kg:-"))

hg = float(input("Enter the height in m:-"))

BMI = float(round(wg/hg**2))

print("BMI = ",BMI)

if BMI<= 18.5 :
    print("They are underweight.")
    
elif BMI<25 :
        print("They have a normal weight.")
        
elif BMI<30 :
        print("They have overweight")
elif BMI<35 :
        print("They are obese.")

else :
    print("They are clinically obese.")
    
print("Thank You....!")

