KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        assert isinstance(kapasiteetti, int)
        assert isinstance(kasvatuskoko, int)
        if kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def maybe_kasvata(self):
        if self.alkioiden_lkm % len(self.ljono) != 0:
            return
        taulukko_old = self.ljono
        self.kopioi_taulukko(self.ljono, taulukko_old)
        self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.ljono)

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            self.maybe_kasvata()
            return True
        return False

    def poista(self, n):
        try:
            self.ljono.remove(n)
        except ValueError:
            return False
        self.alkioiden_lkm -= 1
        self.ljono.append(0)  # necessary or not?
        return True

    def kopioi_taulukko(self, a, b):
        b[0:len(a)] = a[:]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def set_op(a, b):
        return set(a.to_int_list()), set(b.to_int_list())

    @staticmethod
    def to_int_set(T):
        J = IntJoukko()
        for v in T:
            J.lisaa(v)
        return J

    @staticmethod
    def yhdiste(a, b):
        a, b = IntJoukko.set_op(a, b)
        return IntJoukko.to_int_set(a | b)

    @staticmethod
    def leikkaus(a, b):
        a, b = IntJoukko.set_op(a, b)
        return IntJoukko.to_int_set(a & b)

    @staticmethod
    def erotus(a, b):
        a, b = IntJoukko.set_op(a, b)
        return IntJoukko.to_int_set(a - b)

    def __str__(self):
        data = self.ljono[:self.alkioiden_lkm]
        return "{" + ", ".join(map(str, data)) + "}"
