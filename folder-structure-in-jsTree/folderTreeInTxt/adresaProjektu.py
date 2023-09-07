from pathlib import Path

class pathProj:

    def __init__(self):

        self.adresaLoguStr = self.sestavAdresuLogu()
        self.nactiSettings(self.adresaLoguStr)
        self.vymazLog(self.adresaLoguStr)


    def getAdresaLoguStr(self):
        return(self.adresaLoguStr)

    def getPocetCyklu(self):
        return(self.pocetCyklu)

    def getDefaultniAdresa(self):
        return(self.defaultniAdresa)



    def sestavAdresuLogu(self):

        adresaParentSpl = Path.cwd().parent.parts
        adresaParentStr = adresaParentSpl[0]

        for i in range(1, len(adresaParentSpl)):
            slozka = adresaParentSpl[i]
            adresaParentStr = adresaParentStr + slozka + '\\'

        adresaLoguStr = adresaParentStr + 'LogSettings'

        return(adresaLoguStr)


    def nactiSettings(self, adresaLoguStr):

        adresaSettings = adresaLoguStr + '\\settings.txt'
        settingsData = self.nactiDataTxt(adresaSettings)

        try:
            self.pocetCyklu = int(settingsData[0])
            self.defaultniAdresa = settingsData[1].strip()
        except:
            self.pocetCyklu = 1
            self.defaultniAdresa = adresaLoguStr




    def nactiDataTxt(self, adresaSettings):
        pole = []

        r = -1
        with open(adresaSettings, 'r') as f:
            for line in f:
                r = r + 1

                line = line.replace('\n', '')
                pole.append(line)

        return (pole)


    def vymazLog(self, adresaLog):

        souborLog = adresaLog + '\\foldersTree.log'

        f = open(souborLog, 'w')

        f.write("")    # nezapise nic
        f.close()

