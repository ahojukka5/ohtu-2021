from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, siirto):
        return self.tekoaly.anna_siirto()
