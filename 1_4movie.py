class Movie:
 def __init__(self, title, producer, director, releaseDate, length, genre, cost, revenue):
    self.title = title
    self.producer = producer
    self.director = director
    self.releaseDate = releaseDate
    self.length = length
    self.genre = genre
    self.cost = cost
    self.revenue= revenue

 def display_data(self):
     """
     >>> m = Movie("The Hunger Games", "Nina Jacobson", "Gary Ross", "23/03/2012", 144, "Adventure", 78000000, 407999255)
     >>> m.display_data()
     Movie: The Hunger Games
     Producer: Nina Jacobson
     Director: Gary Ross
     Release Date: 23/03/2012
     Length (mins): 144
     Genre: Adventure
     Gross Profit ~: 329999255
     """
     print("Movie:", self.title, "\nProducer:", self.producer, "\nDirector:", self.director, "\nRelease Date:", self.releaseDate, "\nLength (mins):", self.length, "\nGenre:", self.genre, "\nGross Profit ~:", self.revenue - self.cost)

# main routine
if __name__ == "__main__":
 import doctest
 doctest.testmod(verbose = False)
 movie1 = Movie("The Hunger Games", "Nina Jacobson", "Gary Ross", "23/03/2012", 144, "Adventure", 78000000, 407999255)
 movie1.display_data()
