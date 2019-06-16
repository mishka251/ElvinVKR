import copy
import os
import json

def getPercs(count:int):
    dir = os.path.abspath(__file__)
    dir = os.path.dirname(dir)
    filename = dir+"/cache/" +  str(count) + ".txt"
    try:
        f = open(filename, "r")
        s = f.read()
        f.close()
        return json.loads(s)

    except:
        res = calcPercs(count)
        f = open(filename, "w")
        f.write(json.dumps(res))
        f.close()
        return res
        

    pass


def calcPercs(count:int):

    percs = []
    portf= [0]*count
    #portf[count-1]=90
    for i in range(pow(11, count)):
        portf[count-1]+=10
        for i in range(count-1, 0, -1):
            if portf[i]>100:
                portf[i]=0
                portf[i-1]+=10
                pass
            pass
        if sum( portf)==100:
            percs.append(copy.copy(portf))
            pass

       # print(portf)
        pass
    return percs

