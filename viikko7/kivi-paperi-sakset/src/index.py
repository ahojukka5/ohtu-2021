from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


PELIT = {
    "a": KPSPelaajaVsPelaaja,
    "b": KPSTekoaly,
    "c": KPSParempiTekoaly}


def main(pelit=PELIT):
    while True:
        print("Valitse pelataanko")
        print("(a) Ihmistä vastaan")
        print("(b) Tekoälyä vastaan")
        print("(c) Parannettua tekoälyä vastaan")
        print("Muilla valinnoilla lopetetaan")

        vastaus = input()
        if vastaus in pelit:
            print("Peli loppuu kun pelaaja antaa virheellisen "
                  "siirron eli jonkun muun kuin k, p tai s")
            pelit[vastaus]().pelaa()
        else:
            break


if __name__ == "__main__":
    main()
