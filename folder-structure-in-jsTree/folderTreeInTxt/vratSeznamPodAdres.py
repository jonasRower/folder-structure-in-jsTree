import os


class seznamPodAdres:

    def __init__(self, adresaInit):

        seznamPodslozek = self.vratSeznamSlozek(adresaInit)
        self.seznamPodAdres = self.vratSeznamAdres(adresaInit, seznamPodslozek)



    def getSeznamPodAdres(self):
        return(self.seznamPodAdres)



    def vratSeznamAdres(self, adresaInit, vsechnyPodslozky):

        seznamAdres = []

        for i in range(0, len(vsechnyPodslozky)):
            podslozka = vsechnyPodslozky[i]
            celaAdresa = adresaInit + "\\" + podslozka

            seznamAdres.append(celaAdresa)

        return (seznamAdres)



    def vratSeznamSlozek(self, adresaInit):

        # list to store files
        res = []

        # Iterate directory
        for file_path in os.listdir(adresaInit):
            # check if current file_path is a file
            if os.path.isdir(os.path.join(adresaInit, file_path)):
                # add filename to list
                res.append(file_path)

        return (res)