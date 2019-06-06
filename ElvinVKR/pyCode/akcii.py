# -*- coding: utf-8 -*-
import new_finam
import calc
import os
import time
from typing import List


class stock:
    """
    Класс акции
    Есть название акции(русское)
    Код и ид для финама
    Цена(за год и за 3 месяца)
    Получение цен с финама
    Расчёт коэфф. М
    Рассчёт доходности
    """
    name:str = ""
    code:str = ""
    id:int = 0
    pricesYear:List[float] = []
    prices3Months:List[float] = []

    def __init__(self, name:str, code:str, id:int):
        """
        Конструктор - запоминаем 
        название, код и ид
        """
        self.code = code
        self.id = id
        self.name = name
        
    def loadPrices(self)->None:
        """
        Грузим цены с финама
        """
        
        dir = os.path.abspath(__file__)
        dir = os.path.dirname(dir)
        filename = dir+"/cache/" + self.code + str(self.id) + "cache.txt"

        if os.path.exists(filename):# and False:
            f = open(filename, "r")
            l1 = f.readline()
            l2 = f.readline()
            f.close()
            #print(l1)
            s1 = l1.strip("[]\n")
            s2 = l2.strip("[]\n")

            ar1 = s1.split(",")
            ar2 = s2.split(",")
            
            try:
                self.pricesYear = list(map(float, ar1))
                self.prices3Months = list(map(float, ar2))
            except ValueError:
                print("Error")
                print(self.name, self.code)
                print(ar1)
                print(ar2)
                self.pricesYear = []
                self.prices3Months = []


            pass
        else:

            self.pricesYear = new_finam.getVals(code=self.code, em = self.id, df='01', mf='01', yf='2018', dt='01',mt='01', yt='2019')
            #print()
            #print()
            self.prices3Months = new_finam.getVals(code=self.code, em = self.id, df='01', mf='01', yf='2019', dt='01',mt='04', yt='2019')
            
            f = open(filename, "w")
            f.write(str(self.pricesYear))
            f.write("\n")
            f.write(str(self.prices3Months))
            f.close()

            time.sleep(10)#ждем 10 сек чтобы финам нас не банис
        return

    def getMs(self, alph:float=0.05, k:float=0.4)->List[float]:
        """
        Считаем м1, м2 и возвращаем
        """
        return calc.getMs(self.pricesYear, alph, k)

    def getDohod(self)->float:
        """
        Считаем и возвращаем доходность
        """
        st = self.prices3Months[0]
        fi = self.prices3Months[len(self.prices3Months) - 1]
        return (st - fi) / st

    def getInfo(self)->None:
        print(self.code)
        print("for year")
        print(self.pricesYear)
        print("for 3 months")
        print(self.prices3Months)