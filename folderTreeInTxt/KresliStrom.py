import os
import vratSeznamPodAdres
import zapisDataDoLogu
import nactiDataZLogu

class vykresliStrom:

    def __init__(self):

        adresaLog = "tady nastav adresu, kam tisknout txt"
        self.hlavniBeh(adresaLog)


    def hlavniBeh(self, adresaLog):

        for i in range(0, 5):
            self.nacitaniZLogu(adresaLog)


    def nacitaniZLogu(self, adresaLog):

        nacitaniDat = nactiDataZLogu.nactiLog(adresaLog)
        seznamAdresLog = nacitaniDat.getDataLog()

        for i in range(0, len(seznamAdresLog)):
            adresaInit = seznamAdresLog[i]

            self.nacitaniAZapisDoLogu(adresaInit, adresaLog)


    def nacitaniAZapisDoLogu(self, adresaInit, adresaLog):

        ziskejSeznamPodadres = vratSeznamPodAdres.seznamPodAdres(adresaInit)
        seznamPodAdres = ziskejSeznamPodadres.getSeznamPodAdres()

        # zapise data do logu
        zapisDataDoLogu.logujData(adresaLog, seznamPodAdres)



