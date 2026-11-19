from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tavaroita = 0
        self._hinta = 0
        self._ostokset = {}

    def tavaroita_korissa(self):
        return self._tavaroita

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self._tavaroita += 1
        self._hinta += lisattava.hinta()
        nimi = lisattava.nimi()
        if nimi in self._ostokset:
            self._ostokset[nimi].muuta_lukumaaraa(1)
        else:
            self._ostokset[nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        nimi = poistettava.nimi()
        if nimi not in self._ostokset:
            return

        ostos = self._ostokset[nimi]
        ostos.muuta_lukumaaraa(-1)
        self._tavaroita -= 1
        self._hinta -= poistettava.hinta()

        if ostos.lukumaara() == 0:
            del self._ostokset[nimi]

    def tyhjenna(self):
        pass

    def ostokset(self):
        return list(self._ostokset.values())
