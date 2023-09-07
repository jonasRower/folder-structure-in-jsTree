import os
import vratSeznamPodAdres
import zapisDataDoLogu
import nactiDataZLogu

class vykresliStrom:

    def __init__(self, adresaLoguStr, defaultniAdresa, pocetCyklu):

        adresaLog = adresaLoguStr + '\\foldersTree.log'
        self.hlavniBeh(adresaLog, defaultniAdresa, pocetCyklu)


    def hlavniBeh(self, adresaLog, defaultniAdresa, pocetCyklu):

        seznamPodAdres = []
        seznamPodAdres.append(defaultniAdresa)
        zapisDataDoLogu.logujData(adresaLog, seznamPodAdres)

        for i in range(0, pocetCyklu):
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



