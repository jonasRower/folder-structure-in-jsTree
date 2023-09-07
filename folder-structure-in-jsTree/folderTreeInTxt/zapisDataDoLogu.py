import nactiDataZLogu

class logujData:

    def __init__(self, adresaLog, dataKTisku):

        # je potreba nacist puvodni log a zapsat do nej nova data
        nacitaniDat = nactiDataZLogu.nactiLog(adresaLog)
        predchoziData = nacitaniDat.getDataLog()

        dataKTisku = self.slucDataKTiskuDoLogu(predchoziData, dataKTisku)

        self.tiskniDataDoTxt(dataKTisku, adresaLog)


    # je potreba sloucit data tak, aby nebyla duplicitni
    def slucDataKTiskuDoLogu(self, predchoziData, dataKTisku):

        for i in range(0, len(dataKTisku)):
            radek = dataKTisku[i]
            dataObsahujiRadek = self.detekujZdaPoleJizObsahujePolozku(predchoziData, radek)

            if(dataObsahujiRadek == False):
                predchoziData.append(radek)


        return(predchoziData)



    def detekujZdaPoleJizObsahujePolozku(self, pole, polozka):

        try:
            ind = pole.index(polozka)
            if(ind > -1):
                poleObsahujePolozku = True
            else:
                poleObsahujePolozku = False

        except:
            poleObsahujePolozku = False

        return(poleObsahujePolozku)


    def tiskniDataDoTxt(self, dataKTisku, adresaLog):
        dataWrite = ""

        f = open(adresaLog, 'w')

        for i in range(0, len(dataKTisku)):
            radek = str(dataKTisku[i])

            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()