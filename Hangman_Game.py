# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:47:04 2022

@author: gautam
"""
logo ="""
 __                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""" 

print("Let's play Hangman...!!")
print(logo)

import random

my_list = ["gautam", "advark", "jukebox"]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


c_word = random.choice(my_list)

lives = 0

#print(f"The chosen word is {c_word}")

#guess=input("Guess a letter:-").lower()

display = []
for blank in c_word:
   display += "_"
   
#print(display)
 
end_of_game = False

while not end_of_game:
    guess=input("Guess a letter:-").lower()

    for position in range(len(c_word)):
       letter = c_word[position]
       if letter == guess:
          display[position] = letter
       
    if guess not in display:
        lives += 1
        if lives == 6:
            end_of_game = True
            print("you lose.")
    print(display)       
    print(HANGMANPICS[lives])
  
    if "_" not in display:
        end_of_game = True
        print("you win.")
   
print(f"The word was {c_word}") 

       
   
    
