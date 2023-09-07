
from pathlib import Path

class pathProj:

    def __init__(self):

        adresaParentStr = self.sestavAdresuLogu()

        self.adresaLoguStr = adresaParentStr + 'LogSettings'
        self.adresaJsTreeStr = adresaParentStr + 'jsTree'



    def getAdresaLogu(self):
        return(self.adresaLoguStr)

    def getAdresaJsTree(self):
        return(self.adresaJsTreeStr)


    def sestavAdresuLogu(self):
        adresaParentSpl = Path.cwd().parent.parts
        adresaParentStr = adresaParentSpl[0]

        for i in range(1, len(adresaParentSpl)):
            slozka = adresaParentSpl[i]
            adresaParentStr = adresaParentStr + slozka + '\\'


        return (adresaParentStr)


