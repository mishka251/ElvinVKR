import akcii
import numpy
from typing import List, Dict

class Portfel(akcii.stock):
    stocks = []
    percs = []

    def __init__(self, stocks:List[akcii.stock], percs:List[float]):
        self.stocks = stocks
        self.percs = percs
        
        self.code = [st.code for st in stocks]
        self.name = [st.name for st in stocks]

        tmp = [st.pricesYear for st in stocks]
        
        minLen = len(tmp[0]) 
        for i in range(len(tmp)):
            minLen = min([minLen, len(tmp[i])])

        tmp = [ t[0:minLen] for t in tmp]

        tmp1 = [st.prices3Months for st in stocks]
        minLen = len(tmp1[0]) 
        for i in range(len(tmp1)):
            minLen = min([minLen, len(tmp1[i])])

        tmp1 = [ t[0:minLen] for t in tmp1]
        try:
            self.pricesYear = numpy.dot(numpy.transpose(tmp), percs)         
            self.prices3Months = numpy.dot(numpy.transpose(tmp1), percs)
        except:
            print("error in ", list(map(lambda s:s.name, self.stocks)))


    def loadPrices(self):
        pass

    def getInfo(self):
        print(self.percs)
        super(Portfel, self).getInfo()

    def toDict(self):
        ms = self.getMs()
        return {'percs':self.percs, 'names':list(map(lambda st:st.name, self.stocks)), 'm1':ms[0], 'm2':ms[1], 'dohod':self.getDohod() }