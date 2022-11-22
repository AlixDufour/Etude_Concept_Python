import pandas as pd
import matplotlib.pyplot as plt



if __name__ == '__main__':
    patients = pd.read_csv(r'patients.csv')

    # Affichage d'un diagramme en bâton montrant l'occurence d'apparition des labels
    patients["Label"].value_counts().plot.bar();
    plt.legend()
    plt.xlabel("Label")
    plt.ylabel("Occurence")
    plt.show()