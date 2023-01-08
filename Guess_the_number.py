# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:49:13 2022

@author: gautam
"""
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


print("Welcone to number guessing game...!!")

logo = """


  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       

"""
print(logo)


turns = 0

def check_answer(guess, answer, turns):
    if guess>answer:
        print("Too high")
        return turns - 1
    elif guess<answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}, You Win..!!")
    
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    number = list(range(1,101))
    
    answer = random.choice(number)
    print("I'm thinking a number between 1 and 100")
    
    turns = set_difficulty() 
   # print(f"You have {turns} attempt remaining to guess the number.")
    
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempt remaining to guess the number.")
        
        guess =int(input("Make a guess:- "))
        
        turns = check_answer(guess, answer, turns)
         
        if turns == 0:
            print("You have run out of the guesses, You Lose..!")
            return
        else:
            guess != answer
 
    
game()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
