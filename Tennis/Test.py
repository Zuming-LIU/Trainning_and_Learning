# Made by Zuming LIU, the 26/11/2018
# This script is used to run a round of tennis game in which the winner of each point is
# generated randomly

# -*- coding: utf-8 -*-
import random
import time
from player import Player
from game import Game

# Name 2 players for a round of tennis
name_player1 = "Jack";
name_player2 = "Bob";
player1 = Player(name_player1);
player2 = Player(name_player2);
Round = Game(player1,player2);
print ("Round begins, " + name_player1 + " vs " + name_player2 + ":");

# Loop until there is a winner
while (Round._hasWinner() == False):    
    # Generate a random variable to find the winner of a ball
    if (random.random() < 0.5):
        nameWinner = player1.name;
    else:
        nameWinner = player2.name;
        
    # Calculate scores and print results
    Round.winPoint(nameWinner);

# When a winner is founda, quit loop and end this round
winner = Round.winner;
print ('Set, ' + winner.name +  ' wins this round ');

