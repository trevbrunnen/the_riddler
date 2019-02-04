# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:05:43 2019

@author: trevb
"""

import pandas as pd
import numpy as np
import random as rd

"""
For the Riddler Feb, 1, 2019. Plays 1 round of the game. Returns 1 if deck A
wins, returns 0 if deck B win.
"""

def playgame(deckA,deckB,points):
    rd.shuffle(deckA)
    rd.shuffle(deckB)
    winner = False
    i = 0
    APoints = 0
    BPoints = 0
    while(winner == False):
        if(deckA[i]>deckB[i]):
            APoints += 1
        else:
            BPoints += 1
        if(APoints >= points):
            winner = True
            win =1
        elif(BPoints >= points):
            winner = True
            win = 0
        i+=1
    
    
    return win
    

deck1 = [14,14,14,14,9,9,9,9,7,7,7,7]
deck2 = [13,13,13,13,11,11,11,11,6,6,6,6]
deck3 = [12,12,12,12,10,10,10,10,8,8,8,8]

points = 5

trials = 10000000

deck1over2 = 0
deck2over3 = 0
deck3over1 = 0

for i in range(trials):
    if(playgame(deck1,deck2,points) == 1):
        deck1over2 += 1
    if(playgame(deck2,deck3,points) == 1):
        deck2over3 += 1
    if(playgame(deck3,deck1,points) == 1):
        deck3over1 += 1
        
print("Deck 1 beats Deck 2 " + str(deck1over2/trials*100) + "% of the time")      
print("Deck 2 beats Deck 3 " + str(deck2over3/trials*100) + "% of the time")      
print("Deck 3 beats Deck 1 " + str(deck3over1/trials*100) + "% of the time")      

        
        
        
        


    