from Personnage import Personnage

class Mage(Personnage):
    def __init__(self):
        self.nom = "Lux"
        self.pointsVie = 100
        self.pointsMagie = 100


    # Redéfinition de méthode
    def attaquer(self):
        print(self.nom + " lance un sort !")

