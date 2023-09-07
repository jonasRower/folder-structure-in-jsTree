import adresaProjektu
import nactiTxt
import vratPoleIdARodicuId
import generujJsonData
import generujHtml

ziskejAdresu = adresaProjektu.pathProj()
adresaLoguStr = ziskejAdresu.getAdresaLogu()
adresaJsTreeStr = ziskejAdresu.getAdresaJsTree()

ziskejData = nactiTxt.nacitejTxt(adresaLoguStr)
adresyDlePoctuUrovniNadrazene = ziskejData.getAdresyDlePoctuUrovniNadrazene()
dataLog = ziskejData.getDataLog()

poleIdARodicu = vratPoleIdARodicuId.poleIdARodicuId(adresyDlePoctuUrovniNadrazene)
poleId = poleIdARodicu.getPoleId()
poleRodicuId = poleIdARodicu.getPoleRodicuId()

jsonDataTree = generujJsonData.jsonData(adresyDlePoctuUrovniNadrazene, poleId, poleRodicuId, dataLog)
jsonData = jsonDataTree.getPoleRadku()


generujHtml.novyHtml(jsonData, adresaJsTreeStr)


print()