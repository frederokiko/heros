from personnage import Personnage
from de import De
import random
class Hero(Personnage):
    def __init__(self):
        super().__init__()
        self.or_possede = 0
        self.cuir_possede = 0

    def depouiller(self, monstre):
        self.or_possede += monstre.ar
        self.cuir_possede += monstre.cuir

    def se_reposer(self):
        self.__pv = self.calculer_pv()


    def se_soigner(self):
        soin = random.randint(1, 8)  # Soigne de 1 à 8 PV
        self._Personnage__pv = min(self._Personnage__pv + soin, self.calculer_pv()) 