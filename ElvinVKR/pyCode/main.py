import json
from generate import percsAll
from akcii  import stock
import portfel
import random
import sys
import os
from typing import List, Dict, Tuple

def load(inputFile:str="input.json", alph:float=0.05, k:float=0.4)->List[dict]:
    f = open(inputFile, "r",encoding='utf-8')
    arr = json.load(f)
    f.close()
    return arr


def loadStocks(arr:List[Dict])->Tuple[ List[str], Dict[str, stock]]:
    stocks = {}
    names = []

    for i in range(0, len(arr)):
        elem = arr[i]

        st = stock(elem["name"], elem["code"], elem["id"])
       # print(elem['name'], elem['code'])
        st.loadPrices()

        if len(st.prices3Months)<5 or len(st.pricesYear)<5:
            continue

        stocks[elem["code"]] = st
        names.append(elem["code"])
    return (names, stocks)


def createPortfels(percs, names, stocks, leng):
    ports = []
    for p in percs:
        stocksForPorts = [stocks[name] for name in random.sample(names, leng)]
        port = portfel.Portfel(stocksForPorts, p)
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


def saveAll(ports:List[portfel.Portfel], fname)->None:
   toFile = list(map(lambda port:port.toDict(), ports))
   f = open(fname, "w", encoding='utf-8')
   json.dump(toFile, f, ensure_ascii=False)
   f.close()
   return

def saveBest(result, fname)->None:
   
   f = open(fname, "w", encoding='utf-8')
   json.dump(result, f, ensure_ascii=False)
   f.close()
   return

def main(fliename:str, leng:int, alph:float, k:float, outAll, outRes):
   arr1 = load(fliename, alph, k)
   sts = loadStocks(arr1)
   percs = percsAll[leng]
   ports = createPortfels(percs, sts[0], sts[1], leng)
   res = findBest(ports)
   saveAll(ports, outAll)
   saveBest(res, outRes)
   return

if __name__ =="__main__":
    args = sys.argv

    if len(args)!=7:
       print("Error, incorrect args count = "+str(len(args)))
       sys.exit(1)
       
    try:
       filename = str(args[1])
    except ValueError:
       print("Error, incorrect arg1")
       sys.exit(1)

    try:
       leng = int(args[2])
    except ValueError:
       print("Error, incorrect arg2")
       sys.exit(1)

    try:
       alph = float(args[3])
    except ValueError:
       print("Error, incorrect arg3")
       sys.exit(1)

    try:
       k = float(args[4])
    except ValueError:
       print("Error, incorrect arg4")
       sys.exit(1)

    try:
       outAll = str(args[5])
    except ValueError:
       print("Error, incorrect arg5")
       sys.exit(1)

    try:
       outRes = str(args[6])
    except ValueError:
       print("Error, incorrect arg6")
       sys.exit(1)

    main(filename, leng, alph, k, outAll, outRes)
    print("ok")
    sys.exit(0)
