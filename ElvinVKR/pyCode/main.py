import json
from generate import percsAll
from akcii  import stock
import portfel
import random
import sys
import os
from typing import List, Dict, Tuple

#def load(inputFile:str="input.json", alph:float=0.05, k:float=0.4)->List[dict]:
#    f = open(inputFile, "r",encoding='utf-8')
#    arr = json.load(f)
#    f.close()
#    return arr


def loadStocks(leng:int, akc_ids:List[int], akc_codes:List[str]):#->Tuple[ List[str], Dict[str, stock]]:
    stocks = []
    for i in range(0, leng):
        st = stock(akc_codes[i], akc_ids[i])
        st.loadPrices()

        #if len(st.prices3Months)<5 or len(st.pricesYear)<5:
         #   continue
        stocks.append(st)
        #stocks[akc_codes[i]] = st
        #names.append(elem["code"])
    return stocks


def createPortfels(percs:List[float], stocks:List[stock]):
    ports = []
    for p in percs:
        #stocksForPorts = [stocks[name] for name in random.sample(names, leng)]
        port = portfel.Portfel(stocks, p)
        ports.append(port)
    return  ports


def findBest(ports:List[portfel.Portfel]):

    maxM1 = -1000000
    portMaxM1= None
    maxM2 = -1000000
    portMaxM2 = None


    minM1 = 1000000
    portMinM1= None
    minM2 = 1000000
    portMinM2 = None

    for port in ports:
        [m1, m2] = port.getMs()

        if m1>maxM1:
            portMaxM1 = port
            maxM1 = m1

        if m2>maxM2:
            portMaxM2 = port
            maxM2 = m2

        if m1<minM1:
            portMinM1 = port
            minM1 = m1

        if m2<minM2:
            portMinM2 = port
            minM2 = m2  
        continue

    return  {
        'minM1':(minM1, portMinM1.toDict()),
        'minM2':(minM2, portMinM2.toDict()),
        'maxM1':(maxM1, portMaxM1.toDict()),
        'maxM2':(maxM2, portMaxM2.toDict())
         }


def saveAll(ports:List[portfel.Portfel], fname:str)->None:
   toFile = list(map(lambda port:port.toDict(), ports))
   f = open(fname, "w", encoding='utf-8')
   json.dump(toFile, f, ensure_ascii=False)
   f.close()
   pass

def saveBest(result:Dict[str, portfel.Portfel], fname:str)->None:
   
   f = open(fname, "w", encoding='utf-8')
   json.dump(result, f, ensure_ascii=False)
   f.close()
   #pass

def main(leng:int, alph:float, k:float, outAll:str, outRes:str, akc_ids:List[int], akc_codes:List[str]):
   print('main')
   sts = loadStocks(leng, akc_ids, akc_codes)
   print(1)
   percs = percsAll[leng]
   ports = createPortfels(percs, sts)
   res = findBest(ports)
   print(2)
   saveAll(ports, outAll)
   saveBest(res, outRes)
   #pass

if __name__ =="__main__":
    args = sys.argv
    """
    Аргументы
    0 - системное
    1 - альфа
    2 - К
    3 - имя_выхода все портфели
    4 - имя_выхода - лучшие

    5+2*и,6+2*и - ид и-й акции, код и-й акции
    """
    if len(args)<=6 or len(args)%2!=1:
       print("Error, incorrect args count = "+str(len(args)))
       sys.exit(1)
       

    try:
       alph = float(args[1])
    except ValueError:
       print("Error, incorrect arg1 "+args[1])
       sys.exit(1)

    try:
       k = float(args[2])
    except ValueError:
       print("Error, incorrect arg2")
       sys.exit(1)

    try:
       outAll = str(args[3])
    except ValueError:
       print("Error, incorrect arg3")
       sys.exit(1)

    try:
       outRes = str(args[4])
    except ValueError:
       print("Error, incorrect arg4")
       sys.exit(1)

    #print(len(args))
   # for i in range(len(args)):
   #     print(i, args[i])
    akc_cnt = (len(args)-5)//2
    #print(akc_cnt)
    akc_ids = [0] *akc_cnt
    akc_codes = [0]*akc_cnt
    for i in range(akc_cnt):
        #print(i, 5+2*i, 6+2*i)
        #print(args[5+2*i])
        akc_ids[i] = int(args[5+2*i])
        akc_codes[i] = str(args[6+2*i])
        #pass


    main(akc_cnt, alph, k, outAll, outRes, akc_ids, akc_codes)
    print("ok")
    sys.exit(0)
