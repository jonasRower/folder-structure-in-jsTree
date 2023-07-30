class nacitejTxt:

    def __init__(self):
        adresaLog = "zde zadej adresu txt"

        dataLog = self.nactiDataTxt(adresaLog)
        poleNadrazenychAdres = self.vratPoleNadrazenychAdresaru(dataLog)
        potomkyKNadrazenymAdresam = self.vyhhledejPotomkyKeVsemNadrazenymAdresam(dataLog, poleNadrazenychAdres)

        self.adresyDlePoctuUrovniNadrazene = self.vratPocetZanoreniKPotomkumNadrazeneAdresy(potomkyKNadrazenymAdresam)
        self.dataLog = dataLog


    def getAdresyDlePoctuUrovniNadrazene(self):
        return(self.adresyDlePoctuUrovniNadrazene)


    def getDataLog(self):
        return(self.dataLog)


    def vratPocetZanoreniKPotomkumNadrazeneAdresy(self, potomkyKNadrazenymAdresam):

        poleZakladnichAdres = self.ziskejPoleZakladnichAdres(potomkyKNadrazenymAdresam)
        pocetZanoreniPole = self.vytvorPoleUrovni(poleZakladnichAdres)

        adresyDlePoctuUrovniNadrazene = self.seradAdresyDlePoctuUrovni(potomkyKNadrazenymAdresam, pocetZanoreniPole)

        return(adresyDlePoctuUrovniNadrazene)


    def ziskejPoleZakladnichAdres(self, potomkyKNadrazenymAdresam):

        poleZakladnichAdres = []

        for i in range(0, len(potomkyKNadrazenymAdresam)):
            zakladniAdresa = potomkyKNadrazenymAdresam[i][0]
            poleZakladnichAdres.append(zakladniAdresa)

        return(poleZakladnichAdres)



    def seradAdresyDlePoctuUrovni(self, dataLog, pocetZanoreniPole):

        pocetZanoreniPoleUniq = self.unique(pocetZanoreniPole)
        adresyDlePoctuUrovni = []

        for i in range(0, len(pocetZanoreniPoleUniq)):
            pocetZanoreni = pocetZanoreniPoleUniq[i]
            adresyDaneUrovne = self.vratAdresyDaneUrovne(dataLog, pocetZanoreniPole, pocetZanoreni)

            adresyDlePoctuUrovni.append(adresyDaneUrovne)

        return(adresyDlePoctuUrovni)


    def vratAdresyDaneUrovne(self, dataLog, pocetZanoreniPole, zanoreniExp):

        adresyDaneUrovne = []

        for i in range(0, len(pocetZanoreniPole)):
            pocetZanoeeni = pocetZanoreniPole[i]
            if(pocetZanoeeni == zanoreniExp):
                adresa = dataLog[i]
                adresyDaneUrovne.append(adresa)

        return(adresyDaneUrovne)


    # vrati pole, kdy kazdy radek udava pocet zanorteni
    def vytvorPoleUrovni(self, dataLog):

        pocetZanoreniPole = []

        for i in range(0, len(dataLog)):
            radek = dataLog[i]
            pocetZanoreni = self.vratPocetUrovniRadku(radek)

            pocetZanoreniPole.append(pocetZanoreni)

        return(pocetZanoreniPole)


    def vratPocetUrovniRadku(self, radek):

        radekSpl = radek.split('\\')
        pocetZanoreni = len(radekSpl)

        return(pocetZanoreni)


    def vyhhledejPotomkyKeVsemNadrazenymAdresam(self, dataLog, poleNadrazenychAdres):

        jedinecneAdresyNadrazene = self.unique(poleNadrazenychAdres)
        poleVsechPotomku = []

        for i in range(0, len(jedinecneAdresyNadrazene)):
            adresaNadrazena = jedinecneAdresyNadrazene[i]
            polePotomku = self.vyhledejVsechnyPotomkyKNadrazeneAdrese(dataLog, adresaNadrazena, poleNadrazenychAdres)

            poleVsechPotomku.append(polePotomku)

        return(poleVsechPotomku)


    def vyhledejVsechnyPotomkyKNadrazeneAdrese(self, dataLog, nadrazenaAdresaExp, poleNadrazenychAdres):

            # vrat pole potomku
            polePotomku = []
            polePotomku.append(nadrazenaAdresaExp)

            for i in range(0, len(dataLog)):
                nadrazenaAdresa = poleNadrazenychAdres[i]
                if(nadrazenaAdresa == nadrazenaAdresaExp):
                    polePotomku.append(dataLog[i])

            return(polePotomku)


    def vratPolePotomku(self, dataLog, nadrazenaAdresa):

        print()



    def vratPoleNadrazenychAdresaru(self, dataLog):

        poleNadrazenychAdres = []

        for i in range(0, len(dataLog)):
            radek = dataLog[i]
            adresaNadrazena = self.vratNadtrazenouAdresu(radek)

            poleNadrazenychAdres.append(adresaNadrazena)

        return(poleNadrazenychAdres)


    def vratNadtrazenouAdresu(self, adresa):

        adresaSpl = adresa.split('\\')
        adresaNew = ""

        for i in range(0, len(adresaSpl)-1):
            slozka = adresaSpl[i]
            if(i == 0):
                adresaNew = adresaNew + slozka
            else:
                adresaNew = adresaNew + '\\' + slozka

        return(adresaNew)




    def nactiDataTxt(self, adresaLog):
        pole = []

        r = -1
        with open(adresaLog, 'r') as f:
            for line in f:
                r = r + 1

                line = line.replace('\n', '')
                pole.append(line)

        return (pole)



    def unique(self, dataLog):

        # initialize a null list
        unique_list = []

        # traverse for all elements
        for x in dataLog:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)

        return(unique_list)