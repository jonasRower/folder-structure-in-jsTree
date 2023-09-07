
import kresliStrom
import adresaProjektu

ziskejAdresu = adresaProjektu.pathProj()

adresaLoguStr = ziskejAdresu.getAdresaLoguStr()
pocetCyklu = ziskejAdresu.getPocetCyklu()
defaultniAdresa = ziskejAdresu.getDefaultniAdresa()

kresliStrom.vykresliStrom(adresaLoguStr, defaultniAdresa, pocetCyklu)
