import pandas as pd


if __name__ == '__main__':
    print("Ici on extrait les données d'une petite base de données dans un fichier csv")
    patients = pd.read_csv(r'patients.csv')

    print("On peut tout d'abord très facilement l'afficher en entier :")
    print(patients)

    print("\ndescribe() permet de donner en une seule ligne une première analyse des données (moyenne, écart-type, médiane, min, max...) :")
    print(patients.describe())

    print("\non peut aussi en une seule ligne les trier selon une colonne, ici par exemple l'année de naissance :")
    print(patients.sort_values(by=["Naissance"]))

    print("\nEnfin on peut facilement filtrer aussi certaines données, par exemple ici on ne veut afficher que les patients avec le label 4 :")
    print(patients[patients["Label"]==4])