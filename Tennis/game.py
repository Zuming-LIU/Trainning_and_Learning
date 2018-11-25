# This script details the rules to get points and to win a round of Tennis
# -*- coding: utf-8 -*-

class Game:
    # Points to print according to different scores
    points = ["Zero", "Fifteen", "Thirty", "Forty"];
    
    # Initialization a game with 2 players
    def __init__(self, player1, player2):
        self.winner = None;
        self.player1 = player1;
        self.player2 = player2;

    # Take the winner of a point to calculate scores and generate a winner
    def winPoint(self, nameWinner):
        # Identify the winner and loser for this ball
        if(nameWinner == self.player1.name):
            pointWinner = self.player1;
            pointLoser = self.player2;
        elif(nameWinner == self.player2.name):
            pointWinner = self.player2;
            pointLoser = self.player1;
        else:
            print("Error about a player name")

        # Add points and decide winner of a round
        if (pointWinner.score < 3 ): # [0 , 15, 30] vs [0 , 15, 30]
            pointWinner.getScore();
            print (pointWinner.name +  ' wins a point, ' + self.points[self.player1.score] + ' vs ' + self.points[self.player2.score]);

        elif (pointWinner.score == 3):
            if (pointLoser.score <= 2 or pointWinner._hasAdvanture): #40 vs [0 , 15, 30]
                self.winner = pointWinner;
            elif (pointLoser.score == 3 and pointLoser._hasAdvanture):# 40 vs AD and the one with AD fails
                pointLoser.loseAdvantage();
                print (pointWinner.name +  ' wins a point,' + self.points[self.player1.score] + ' vs ' + self.points[self.player2.score]);
            else:   #40 vs 40, set advantage
                pointWinner.getAdvantage();
                print (pointWinner.name +  ' wins a point and he(she) gets the advantage ! ')
    
        else:
            print ("Error of score, overflow");
   
    def _hasWinner(self):
        if (self.winner == None):
            return False;
        else:
            return True;



