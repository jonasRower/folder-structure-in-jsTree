import nactiTxt
import vratPoleIdARodicuId
import generujJsonData
import generujHtml

ziskejData = nactiTxt.nacitejTxt()
adresyDlePoctuUrovniNadrazene = ziskejData.getAdresyDlePoctuUrovniNadrazene()
dataLog = ziskejData.getDataLog()

poleIdARodicu = vratPoleIdARodicuId.poleIdARodicuId(adresyDlePoctuUrovniNadrazene)
poleId = poleIdARodicu.getPoleId()
poleRodicuId = poleIdARodicu.getPoleRodicuId()

jsonDataTree = generujJsonData.jsonData(adresyDlePoctuUrovniNadrazene, poleId, poleRodicuId, dataLog)
jsonData = jsonDataTree.getPoleRadku()


generujHtml.novyHtml(jsonData)


print()