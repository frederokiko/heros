from dragonnet import Dragonnet
from foret import Foret
from humain import Humain
from loup import Loup
from nain import Nain
from orque import Orque
import random

def main():
    foret = Foret()
    foret.ajouter_hero(Humain())
    for _ in range(5):
        foret.ajouter_monstre(random.choice([Loup(), Orque(), Dragonnet()]))
    foret.combat()

if __name__ == "__main__":
    main()