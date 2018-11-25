# Define the class of a player with his name

# -*- coding: utf-8 -*-
class Player:

    def __init__(self, name):
        self.name = name;
        self.score = 0;
        self._hasAdvanture = False;
        
    def getScore(self):
        self.score = self.score + 1;
        
    def loseAdvantage(self):
        self._hasAdvanture = False;

    def getAdvantage(self):
        self._hasAdvanture = True;
