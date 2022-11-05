
class Personnage :
    def __init__(self):
        self.nom = "Rakan"
        self.pointsVie = 100

    def attaquer(self):
        print(self.nom + " attaque")

    # Opérateur <
    def __lt__(self, other):
        return self.pointsVie < other.pointsVie

    #Opérateur <=
    def __le__(self, other):
        return self.pointsVie <= other.pointsVie

    # Opérateur >
    def __gt__(self, other):
        return self.pointsVie > other.pointsVie
    #Opérateur >=

    def __ge__(self, other):
        return self.pointsVie >= other.pointsVie

    def __eq__(self, other):
        return self.pointsVie == other.pointsVie