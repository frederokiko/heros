import random
from de import De
class Personnage:
    def __init__(self):
        self.__force = self.calculer_caracteristique()
        self.__endurance = self.calculer_caracteristique()
        self.__pv = self.calculer_pv()

    @property
    def force(self):
        return self.__force

    @property
    def endurance(self):
        return self.__endurance

    def calculer_caracteristique(self):
        de = De(1, 6)
        jets = [de.lance() for _ in range(4)]
        return sum(sorted(jets, reverse=True)[:3])

    def calculer_pv(self):
        return self.endurance + self.modificateur(self.endurance)

    def modificateur(self, caracteristique):
        if caracteristique < 5:
            return -1
        elif caracteristique < 10:
            return 0
        elif caracteristique < 15:
            return 1
        else:
            return 2

    def frappe(self, cible):
        de = De(1, 4)
        degats = de.lance() + self.modificateur(self.force)
        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.__pv -= degats

    def est_mort(self):
        return self.__pv <= 0
