from Guerrier import Guerrier
from Mage import Mage
from Archer import Archer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # Création d'une liste d'entier
    ListeNombre = [5,7,6,9,10]

    # Appel de la méthode de tri sur des nombres entier
    ListeNombre.sort()
    print(ListeNombre)

    lux = Mage()
    garen = Guerrier()
    ashe = Archer()

    lux.pointsVie -= 10

    # Création d'une liste de personnage
    ListePersonnage = [garen, ashe, lux]
    print("Liste personnage avant tri :")
    print(ListePersonnage)

    # Appel de la méthode de tri sur des personnages => L'objet liste peut utiliser cette méthode sur n'importe quel type de données
    # Tant que les opérateurs de comparaisons ont été surchargés
    ListePersonnage.sort()
    print("Liste personnage après tri :")
    print(ListePersonnage)