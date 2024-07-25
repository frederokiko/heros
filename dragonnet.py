from monstre import Monstre
from de import De
class Dragonnet(Monstre):
    def __init__(self):
        super().__init__()
        self.cuir = De(1, 4).lance()

    @property
    def endurance(self):
        return super().endurance + 1