class BasketballPlayer:
 def __init__(self, name, goals, games):
    self.name = name
    self.standard_goals = goals
    self.games = games

 def get_average(self):
     """
     >>> b = BasketballPlayer("Karen", 100, 20)
     >>> b.get_average()
     5.0
     """
     return self.standard_goals / self.games

 def display_average(self):
     """
     >>> b = BasketballPlayer("Karen", 100, 20)
     >>> b.get_average()
     The average goals scored per game by Karen is 5.0
     """
     print("The average goals scored per game by", self.name, "is", self.standard_goals / self.games)

def best_player():
    best.append(ball1.get_average())
    best.append(ball2.get_average())
    best.append(ball3.get_average())

# main routine
if __name__ == "__main__":
 import doctest
 doctest.testmod(verbose = False)
 best = []
 ball1 = BasketballPlayer("Karen", 100, 20)
 ball2 = BasketballPlayer("Perry", 24, 80)
 ball3 = BasketballPlayer("Megan", 55, 66)
 ball1.display_average()
 ball2.display_average()
 ball3.display_average()
 best_player()
 print(max(best))
