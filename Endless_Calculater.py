# -*- coding: utf-8 -*-
"""
Created on Mon May  9 07:35:02 2022

@author: gautam
"""
#Calculator:-



logo = """

 _____________________
|  _________________  |
| | GP          0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|


"""

#Add:
    
def add(n1, n2):
    return n1+n2

#Subtract:
    
def subtract(n1, n2):
    return n1-n2

#Multiply:
    
def multiply(n1, n2):
    return n1*n2

#Division:
    
def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,}

def calculator():
    num1 = float(input("What's the first number?: "))
    
    for symbol in operations:
        print(symbol)
        
    should_continue = True
    
    while should_continue:
        
        operation_symbol = input("Pick another operation:- ")
        num2 = float(input("What's the next number?: "))
        calculation_functions = operations[operation_symbol]
        answer = calculation_functions(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        should_continue = input(f"Type 'y' to calculationg with {answer}, or type 'n' to start a new calculation:- ")
        
        if should_continue == "y":
            num1 = answer
        
        else:
            should_continue = False
            calculator()

calculator()
        
        
        
        
        
        
        
        
        
        
        