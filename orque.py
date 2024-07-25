from monstre import Monstre
class Orque(Monstre):
    def __init__(self):
        super().__init__()

    @property
    def force(self):
        return super().force + 1