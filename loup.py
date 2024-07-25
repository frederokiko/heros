from monstre import Monstre
from de import De
class Loup(Monstre):
    def __init__(self):
        super().__init__()
        self.cuir = De(1, 4).lance()