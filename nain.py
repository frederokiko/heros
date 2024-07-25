from hero import Hero
class Nain(Hero):
    def __init__(self):
        super().__init__()

    @property
    def endurance(self):
        return super().endurance + 2