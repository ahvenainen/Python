"""
KT5

Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. Kirjoita seuraavat funktiot:

LueAutot - Lukee näppäimistöltä ensin auton rekisterinumeron ja sitten rekisteröintipäivämäärän ja tallentaa tiedot dictionaryyn.
Tätä toistetaan niin kauan kunnes rekisterinumeroksi syötetään LOPPU.
Päivämäärät tallennetaan datetime-tyyppisinä. Funktio palauttaa täytetyn dictionaryn.
datetime-tyypin käyttö on opiskeltava omatoimisesti. Päivämäärä syötetään muodossa dd.mm.yyyy, siis esimerkiksi 14.1.2022.
Rekisteröintipäivämäärä pyydetään syöttämään uudestaan mikäli päivämäärä on väärässä muodossa.

TalletaTiedostoon - Saa parametrina edellisen dictionaryn ja tallenta sen sisällön tekstitiedostoon autot.txt.
Tiedostossa päivämäärät eivät sisällä kellonaikaa. Tiedoston kukin rivi sisältää auton rekisterinumeron ja rekisteröintipäivämäärän '\t'-merkillä erotettuna

LueTiedostosta - Lukee autot.txt:n dictionaryyn ja palauttaa sen.

TulostaTiedot - Saa parametrinaan dictionaryn joka sisältää rekisteröintitiedot. Funktio tulostaa autojen rekisterinumerot ja rekisteröintipäivämäärät.

Kirjoita tarvittaessa testiohjelma funktioiden testaamiseksi.

VINKKI: Jos luet tiedostoa f rakenteella

for line in f:
   ...

niin muuttuja line sisältää myös rivinvaihdon. Sen voit poistaa str.strip()-metodilla.

"""
# Write functions, define global variables, and import modules here!

import datetime as dt


def LueAutot():
    tiedot = {}

    while True:
        reknum = input("Rekisterinumero: ")
        if reknum.upper() == "LOPPU":
            break
        while True:
            try:
                rekpvm = dt.datetime.strptime(input("Syötä rekisteröintipäivämäärä : "), "%d.%m.%Y")
                tiedot[reknum] = rekpvm
                break
            except ValueError:
                print("Väärin. Syötä päivämäärä uudestaan.")

    return tiedot


def TalletaTiedostoon(autot):
    filepath = "autot.txt"

    try:
        wfile = open(filepath, "wt")
        for key, value in autot.items():
            wfile.write(key + "\t" + value.strftime("%d.%m.%Y") + "\n")
        wfile.close()
    except FileNotFoundError:
        print("Tiedostoa ei voitu avata")


def LueTiedostosta():
    filepath = "autot.txt"
    autot_info = {}

    try:
        rfile = open(filepath, "rt")
        line = rfile.readlines()
        for info in line:
            kilpi = info.split("\t")[0]
            rekpv = info.split("\t")[1].strip("\n")
            autot_info[kilpi] = rekpv
        rfile.close()
    except FileNotFoundError:
        print("Tiedostoa ei voitu avata")

    return autot_info


def TulostaTiedot(tulosta):
    for key, value in tulosta.items():
        print(key, ' : ', value)


if __name__ == "__main__":
    # Write main program below this line
    tiedot1 = LueAutot()
    TalletaTiedostoon(tiedot1)
    autot1 = LueTiedostosta()
    TulostaTiedot(autot1)
