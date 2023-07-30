
class nactiLog:

    def __init__(self, adresaLog):

        self.dataLog = self.nactiDataTxt(adresaLog)


    def getDataLog(self):
        return(self.dataLog)




    def nactiDataTxt(self, adresaLog):

        pole = []

        r = -1
        with open(adresaLog, 'r') as f:
            for line in f:
                r = r + 1

                line = line.replace('\n' ,'')
                pole.append(line)

        return (pole)