import new_finam
import calc
import os
import time

class stock:
    """
    ����� �����
    ���� �������� �����(�������)
    ��� � �� ��� ������
    ����(�� ��� � �� 3 ������)
    ��������� ��� � ������
    ������ �����. �
    ������� ����������
    """
    name = ""
    code = ""
    id = 0
    pricesYear = []
    prices3Months=[]

    def __init__(self, name, code, id):
        """
        ����������� - ���������� 
        ��������, ��� � ��
        """
        self.code=code
        self.id=id
        self.name=name
        
    def loadPrices(self):
        """
        ������ ���� � ������
        """

        filename = self.code+str(self.id)+"cache.txt"

        if os.path.exists(filename):
            f = open(filename, "r")
            f.close()
            pass
        else:

            self.pricesYear = new_finam.getVals(code=self.code, em = self.id, df='01', mf='01', yf='2018', dt='01',mt='01', yt='2019' )
            self.prices3Months = new_finam.getVals(code=self.code, em = self.id, df='01', mf='01', yf='2019', dt='01',mt='04', yt='2019' )
            time.sleep(10)
            f = open(filename, "w")
            f.write(self.pricesYear)
            f.write(prices3Monts)
            f.close()

        return

    def getMs(alph, k):
        """
        ������� �1, �2 � ����������
        """
        return calc.getMs(pricesYear, alph, k)

    def getDohod():
        """
        ������� � ���������� ����������
        """
        st = prices3Months[0]
        fi = prices3Months[len(prices3Months)-1]
        return (st-fi)/st
