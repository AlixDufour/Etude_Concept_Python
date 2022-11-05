from Personnage import Personnage

class Archer(Personnage):
    def __init__(self):
        self.nom = "Ashe"
        self.pointsVie = 100
        self.nombreFleches = 10

    def attaquer(self):
        print(self.nom + " tire une flèche !")

