"""

Ohjelmalla hallinnoidaan yrityksen tuotteita.
Kaikilla tuotteilla on samat yhteiset ominaisuudet: nimi, hinta, hyllypaikka sekä koodi.
Nämä esitellään tuote-luokassa, jonka aliluokat perivät. Aliluokkia on kolme, joilla on omia ominaisuuksia:

a.                         vaate: koko, materiaali
b.                         ruoka: maa, paivays
c.                         kodinkone: takuu, paino 

Ohjelmassa syötetään tuotteita yhdelle tuotelistalle sekä lopuksi tulostetaan koko listan sisältö.
Ohjelmassa ensin valitaan minkä tyyppistä tuotetta ollaan syöttämässä, jonka jälkeen tiedot täytetään.

"""

from datetime import datetime
#Write class and imports here!

class tuote:
    def __init__(self, nimi, hinta, hylly, koodi):
        self.nimi = nimi
        self.hinta = hinta
        self.hylly = hylly
        self.koodi = koodi


    @property
    def nimi(self):
        return self._nimi

    @nimi.setter
    def nimi(self, value):
        self._nimi = value

    @property
    def hinta(self):
        return self._hinta

    @hinta.setter
    def hinta(self, value):
        if value < 0:
            value = 0
        self._hinta = value

    @property
    def hylly(self):
        return self._hylly

    @hylly.setter
    def hylly(self, value):
        self._hylly = value

    @property
    def koodi(self):
        return self._koodi

    @koodi.setter
    def koodi(self, value):
        self._koodi = value

class vaate(tuote):
    def __init__(self, nimi, hinta, hylly, koodi, koko, materiaali):
        super().__init__(nimi, hinta, hylly, koodi)
        self.koko = koko
        self.materiaali = materiaali

    def __str__(self):
        super().__str__()
        print("Nimi:", self.nimi)
        print("Hinta:", self.hinta)
        print("Hylly:", self.hylly)
        print("Koodi:", self.koodi)
        print("Koko:", self.koko)
        print("Materiaali:", self.materiaali)
        return ""


class ruoka(tuote):
    def __init__(self, nimi, hinta, hylly, koodi, maa, paivays=datetime.now().strftime("%d.%m.%Y")):
        super().__init__(nimi, hinta, hylly, koodi)
        self.maa = maa
        self.paivays = paivays

    def __str__(self):
        super().__str__()
        print("Nimi:", self.nimi)
        print("Hinta:", self.hinta)
        print("Hylly:", self.hylly)
        print("Koodi:", self.koodi)
        print("Alkuperä:", self.maa)
        print("Päiväys:", self.paivays)
        return ""

class kodinkone(tuote):
    def __init__(self, nimi, hinta, hylly, koodi, takuu, paino):
        super().__init__(nimi, hinta, hylly, koodi)
        self.takuu = takuu
        self.paino = paino

    def __str__(self):
        super().__str__()
        print("Nimi:", self.nimi)
        print("Hinta:", self.hinta)
        print("Hylly:", self.hylly)
        print("Koodi:", self.koodi)
        print("Takuu:", self.takuu)
        print("Paino:", self.paino)
        return ""

if __name__ == "__main__":
    # Main program here!
    tuotelista = []

    while True:
        valinta = input("\nMikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: ")
        if not (valinta == '1' or valinta == '2' or valinta == '3'):
            print()
            break
        tuote = input("Anna tuotteen nimi: ")
        hinta = float(input("Anna hinta: "))
        hylly = input("Anna hyllypaikka: ")
        koodi = input("Anna koodi: ")
        if valinta == '1':
            maa = input("Ruoan alkuperämää: ")
            pvmS = input("Päivys: ")
            tuotelista.append(ruoka(tuote, hinta, hylly, koodi, maa, pvmS))
        elif valinta == '2':
            koko = input("Vaateen koko: ")
            materiaali = input("Vaateen materiaali: ")
            tuotelista.append(vaate(tuote, hinta, hylly, koodi, koko, materiaali))
        elif valinta == '3':
            takuu = input("Kodinkoneen takuu: ")
            paino = input("Kodinkoneen paino: ")
            tuotelista.append(kodinkone(tuote, hinta, hylly, koodi, takuu, paino))

    for i in tuotelista:
        print(i)
