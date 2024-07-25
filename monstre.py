from personnage import Personnage
from de import De
class Monstre(Personnage):
    def __init__(self):
        super().__init__()
        self.ar = De(1, 6).lance()
        self.cuir = 0