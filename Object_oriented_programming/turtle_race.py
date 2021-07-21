# Turtle Race 

import turtle
import random
import time
class Player:
    """ Racer Registration Attributes"""
    def __init__(self, name='Not Mentioned', color='black'):
        self.name = name
        self.dist_covered = 0
        self.racer = turtle.Turtle()
        self.racer.color(color)
        self.racer.shape('turtle')

    def penup(self):
        self.racer.penup()
    
    def pendown(self):
        self.racer.pendown()

    def forward(self, dist):
        self.racer.forward(dist)
    
    def goto(self, x, y):
        self.racer.goto(x,y)

class RaceGame:
    """ Race Game Simulation """
    def __init__(self, players=['coach']):
        self.screen = turtle.Screen()
        self.screen.title('Turtle Race')
        self.racers = self.register(players)
        self.make_positions(self.racers)
    

    def register(self, players):
        """ Returns list of Player objects """
        COLOURS = ['black','green', 'orange', 'red','skyblue', 'brown', 'gray', 'white']
        self.racers = [None]*len(players)
        for i in range(len(players)):
            player_name = players[i]
            player_color = COLOURS[i%(len(players))]
            self.racers[i] = Player(player_name, player_color)  # Instantiate Player object
        return self.racers

    def make_positions(self, racers, separating_space = 30):
        players_above_y = len(racers)//2
        self.y_position = players_above_y*separating_space
        for racer in racers:
            racer.penup()
            racer.goto(-200, self.y_position)
            racer.pendown()
            self.y_position  = self.y_position - separating_space
        
    
    def run(self, checkpoints=30):
        self.checkpoints = checkpoints

        for i in range(checkpoints):
            for player in self.racers:
                x = random.randint(1,10)
                player.forward(x)
                player.dist_covered+=x
            time.sleep(0.1)
            
        self.report_winner()
    
    def report_winner(self):
        winner = [0,None]
        for player in self.racers:
            if player.dist_covered>winner[0]:
                winner = [player.dist_covered, player.name]
        self.screen.title(f"Turtle Race:  WINNER {winner[1]} 🥇 [Distance Covered:{winner[0]}]")
        self.screen.exitonclick()
        print(f"Winner is {winner[1]}.   Distance Covered:{winner[0]}")
        

if __name__=='__main__':
    PLAYERS = ["Chintu", "Pintu", "Chinni"]
    game = RaceGame(PLAYERS)
    game.run()
