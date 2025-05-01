class Calcul:
    def __init__(self,**kw):
        self.n_mile = kw["n"]

    def calculate(self):
        n_km = self.n_mile * 1.609344
        return n_km