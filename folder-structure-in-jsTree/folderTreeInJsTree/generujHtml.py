class novyHtml:

    def __init__(self, jsonData, adresaJsTreeStr):

        poleRadkuAll = self.vytvorPoleRadkuHtml(jsonData)
        adresaJsTree = adresaJsTreeStr + '\\index.html'
        self.tiskniDataDoTxt(poleRadkuAll, adresaJsTree)

        print()



    def vytvorPoleRadkuHtml(self, jsonData):

        poleRadkuAll = []

        radkyPred = self.definujRadkyPred()
        radkyZa = self.definujRadkyZa()

        poleRadkuAll = radkyPred
        poleRadkuAll = poleRadkuAll + jsonData
        poleRadkuAll = poleRadkuAll + radkyZa

        return(poleRadkuAll)


    def tiskniDataDoTxt(self, dataKTisku, adresaHtml):
        dataWrite = ""

        f = open(adresaHtml, 'w')

        for i in range(0, len(dataKTisku)):
            radek = str(dataKTisku[i])

            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()



    def definujRadkyPred(self):

        radkyPred = []
        radkyPred.append('<!DOCTYPE html>')
        radkyPred.append('<html lang="en" xmlns="http://www.w3.org/1999/xhtml">')
        radkyPred.append('<head>')
        radkyPred.append('    <meta charset="utf-8" />')
        radkyPred.append('    <title>Simple jsTree</title>')
        radkyPred.append('    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jstree/3.2.1/themes/default/style.min.css" />')
        radkyPred.append('    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.js"></script>')
        radkyPred.append('    <script src="https://cdnjs.cloudflare.com/ajax/libs/jstree/3.2.1/jstree.min.js"></script>')
        radkyPred.append('')
        radkyPred.append('    <script type="text/javascript">')
        radkyPred.append('        $(function () {')
        radkyPred.append('')
        radkyPred.append('            var jsondata = [')

        return(radkyPred)


    def definujRadkyZa(self):

        radkyZa = []
        radkyZa.append('            ];')
        radkyZa.append('            createJSTree(jsondata);')
        radkyZa.append('        });')
        radkyZa.append('')
        radkyZa.append('        function createJSTree(jsondata) { ')
        radkyZa.append('            $(\'#SimpleJSTree\').jstree({')
        radkyZa.append('                \'core\': {')
        radkyZa.append('                    \'data\': jsondata')
        radkyZa.append('                }')
        radkyZa.append('            });')
        radkyZa.append('        }')
        radkyZa.append('    </script>')
        radkyZa.append('')
        radkyZa.append('</head>')
        radkyZa.append('<body>')
        radkyZa.append('   <div id="SimpleJSTree"></div>')
        radkyZa.append('</body>')
        radkyZa.append('</html>')

        return (radkyZa)


