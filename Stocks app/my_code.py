"""
KT2


Olet aloittanut osakesijoittamisen ja haluat arvioida sijoituksesi arvoa.
Ohjelmalla (pääohjelmassa) on lista, johon käyttäjä voi lisätä Osake-olioita.
Ohjelma kysyy käyttäjältä ”Lisätäänkö uusi osake (k/e)”.
Kun osakkeet on lisätty listaan, kysyy ohjelma käyttäjältä kuvitteellisen kasvuprosentin sekä ajanjakson vuosina.


Tee luokka Osake, jolla on jäsenmuuttujat:
- nimi
- ostohinta (>0, osakekohtainen ostohinta)
- maara (> 0, omistettujen osakkeiden lkm)



Osakkeella on metodit:

- tulosta_arvo, jonka parametreina on kasvuprosentti ja ajanjakso vuosina (tässä järjestyksessä).
tulosta_arvo-metodi kutsuu toista Osake-luokan metodia laske_tuotto_yhdelle_vuodelle, joka laskee vuosikohtaisen tuoton
tulosta_arvo kutsuu laske_tuotto_yhdelle_vuodelle-metodia vuosien lukumäärän verran.
Siis, jos lasketaan tuottoa kolmelle vuodelle, niin laske_tuotto_yhdelle_vuodelle kutsutaan kolme kertaa.
Huomioi "korkoa korolle". Valuutat tulostetaan kahden desimaalin tarkkuudella.

- laske_tuotto_yhdelle_vuodelle -metodi palauttaa tuoton yhdelle vuodelle.
Metodi on staattinen ja saa parametrinaan kasvuprosentin ja hinnan vuoden alussa (tässä järjesyksessä).

Laske pääohjelmassa  myös koko osakepotin arvo(sama % ja samat vuodet) käymällä lista läpi eli 
joudut miettimään sitä, miten pääohjelmaan palautetaan tieto yhden osakkeen potin arvosta vuosien jälkeen.

Esimerkkiajo:


Anna osakkeen nimi: Nokia
Anna osakkeen ostohinta/kpl: 10
Anna ostettujen osakkeiden lukumäärä: 1000
Lisää osakkeita (k/e)? k

Anna osakkeen nimi: Fortum
Anna osakkeen ostohinta/kpl: 12
Anna ostettujen osakkeiden lukumäärä: 127
Lisää osakkeita (k/e)? e

Anna kasvuprosentti: 5
Anna vuodet: 3

Nokia 1000 10.0
Osakkeen potin arvo on 11576.25 ja tuotto 1576.25

Fortum 127 12.0
Osakkeen potin arvo on 1764.22 ja tuotto 240.22

Koko potin arvo on 13340.47
"""
# Write class and imports here!


class Osake:

    def __init__(self, nimi, ostohinta, maara):
        self.nimi = nimi
        self.ostohinta = ostohinta
        self.maara = maara

    def tulosta_arvo(self, kasvuprosentti, aika):

        # kutsutaan laske_tuotto_yhdelle_vuodelle metodia "aika" -parametrin sisältämän luvun verran.
        arvo = self.maara * self.ostohinta  # alkuarvona maara * ostohinta
        y = 0
        while y < aika:
            arvo += self.laske_tuotto_yhdelle_vuodelle(kasvuprosentti, arvo)  # kasvatetaan "arvo" -muuttujaa.
            y += 1
        tuotto = arvo - self.ostohinta * self.maara
        print(f"Osakkeen potin arvo {arvo:.2f} ja tuotto {tuotto:.2f}")
        return arvo

    # metodi saa kaksi parametria ja palauttaa laskutoimituksen.
    def laske_tuotto_yhdelle_vuodelle(self, kasvuprosentti, arvo):
        return arvo * kasvuprosentti / 100


if __name__ == "__main__":
    # Write main program here
    osakkeet = list()
    kokoPotti = 0
    while True:
        # kerätään tietoja listaan "osakkeet", kunnes käyttäjä syöyttää "e".
        nimi = input("\nAnna osakkeen nimi: ")
        ostohinta = float(input("Anna osakkeen ostohinta/kpl "))
        if ostohinta < 0:
            ostohinta = 0
        maara = int(input("Anna ostettujen osakkeiden lukumäärä: "))
        if maara < 0:
            maara = 0
        osakeOlio = Osake(nimi, ostohinta, maara)  # luodaan olio kutsumalla "Osake" -luokkaa.
        osakkeet.append(osakeOlio)  # lisätään luotu olio "osakkeet" -listaan

        lisaa = input("Lisää osakkkeita (k/e)? ")
        if lisaa.upper() == "E":
            break
        else:
            continue

    kasvupros = float(input("\nAnna kasvuprosentti: "))
    vuodet = int(input("Anna vuodet: "))

    for x in osakkeet:  # haetaan tiedot listasta
        print(f"\n{x.nimi} {x.maara} {x.ostohinta}")
        arvo = x.tulosta_arvo(kasvupros, vuodet)
        kokoPotti += arvo

    print(f"\nKoko potin arvo on {kokoPotti:.2f}")
