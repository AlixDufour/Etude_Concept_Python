from Personnage import Personnage

class Guerrier(Personnage):
    def __init__(self):
        self.nom = "Garen"
        self.pointsVie = 100
        self.endurance = 100

    def attaquer(self):
        print(self.nom + " donne un coup d'épée !")

    # Ne fonctionne pas car on ne peut pas surcharger les méthode en python
    #def attaquer(self, cible : Personnage):
        #print(self.nom + " donne un coupe d'épée à " + cible.nom + " !")
