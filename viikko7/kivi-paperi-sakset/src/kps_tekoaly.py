from kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):

    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, siirto):
        return self.tekoaly.anna_siirto()
