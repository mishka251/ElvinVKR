from typing import List

def getVAR(prices:List[float], alph:float):
    pr = prices[:]
    pr.sort()
    n = len(pr)
    VARmin = pr[int(round(n * alph))]
    VARplus = pr[int(round(n - n * alph))]

    return [VARmin, VARplus]

def getCVAR(prices:List[float], alph:float):
    pr = prices[:]
    pr.sort()
    n = len(pr)
    intval = int(round(n * alph))
    CVARmin = sum([pr[i] for i in range(0, intval)]) / intval
    CVARplus = sum([pr[i] for i in range(n - intval, n)]) / intval

    return [CVARmin, CVARplus]

def getMs(prices:List[float], alph:float, k:float):
    [varM, varP] = getVAR(prices, alph)
    [CvarM, CvarP] = getCVAR(prices, alph)

    m1 = k * varM + (1 - k) * CvarM
    m2 = k * varP + (1 - k) * CvarP

    return [m1, m2]