# Made by Zuming LIU, the 26/11/2018
# This script details the rules to get points and to win a round of Tennis
# -*- coding: utf-8 -*-

class Game:
    # Points to print according to different scores
    points = ["love", "15", "30", "40"];
    
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
        else:
            pointWinner = self.player2;
            pointLoser = self.player1;


        # Add points and decide winner of a round
        if (pointWinner.score < 3 ): # [0 , 15, 30] vs [0 , 15, 30]
            pointWinner.getScore();
            print (pointWinner.name +  ' wins a point, ' + self.points[self.player1.score] + ' vs ' + self.points[self.player2.score]);

        elif (pointWinner.score == 3):
            #40 vs [0 , 15, 30] or 40 vs AD and the one with AD wins
            if (pointLoser.score <= 2 or pointWinner._hasAdvanture): 
                self.winner = pointWinner;
            # 40 vs AD and the one with AD fails
            elif (pointLoser.score == 3 and pointLoser._hasAdvanture):
                pointLoser.loseAdvantage();
                print (pointWinner.name +  ' wins a point, ' + self.points[self.player1.score] + ' vs ' + self.points[self.player2.score]);
            #40 vs 40, set advantage
            else:   
                pointWinner.getAdvantage();
                print (pointWinner.name +  ' wins a point, he(she) gets the advantage ! ');
    
        else:
            print ("Error of score, overflow");
   
    def _hasWinner(self):
        if (self.winner == None):
            return False;
        else:
            return True;



