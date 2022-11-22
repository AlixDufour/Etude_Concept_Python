from Guerrier import Guerrier
from Mage import Mage
from Archer import Archer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    ListeNombre = [5,7,6,9,10]

    ListeNombre.sort()
    print(ListeNombre)

    lux = Mage()
    garen = Guerrier()
    ashe = Archer()

    lux.pointsVie -= 10


    ListePersonnage = [garen, ashe, lux]
    print("Liste personnage avant tri :")
    print(ListePersonnage)
    ListePersonnage.sort()
    print("Liste personnage après tri :")
    print(ListePersonnage)