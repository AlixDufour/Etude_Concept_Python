from Guerrier import Guerrier
from Mage import Mage
from Archer import Archer



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lux = Mage()
    garen = Guerrier()
    ashe = Archer()

    # Redéfinition des méthodes : Chaque classe fills possède sa propre implémentation de la méthode attaquer()
    lux.attaquer()
    garen.attaquer()
    ashe.attaquer()

    lux.pointsVie += 10

    # Surcharge des opérateurs de comparaison
    if(lux > garen):
        print(lux.nom + " a plus de vie que " + garen.nom)
    elif(lux < garen) :
        print(lux.nom + " a moins de vie que " + garen.nom)
    elif(lux == garen):
        print(lux.nom + " a autant de vie que " + garen.nom)

