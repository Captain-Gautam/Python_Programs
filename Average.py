# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:35:03 2022

@author: gautam
"""
#To calculate the average height using loops...!!
# To easy this we can use sum() & len() functio to easy the codes the directly.


print("To calculate the average height using loops...!!")

s_heights = input("Enter the height of the student:-").split()

for n in range(0, len(s_heights)) :
    s_heights[n] = int(s_heights[n])
    
print(s_heights)

# To find the sum of the list :
sum = 0
for num in s_heights :
    s_sum = num
    sum = sum + s_sum  
    
# to find the length of the list :
count = 0    
for length in s_heights :
#    l = length
    count = count + 1
        
#print(count)

#np = len(s_heights)

avg = round(sum/count, 2)

print(f"Average height is {avg}cm.")

