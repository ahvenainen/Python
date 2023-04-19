"""

Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. 

"""


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
