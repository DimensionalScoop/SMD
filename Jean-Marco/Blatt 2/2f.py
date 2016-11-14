import ROOT
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class random_lcd:

    def __init__(self,a,b,m,x0):
        self.__a=a
        self.__b=b
        self.__m=m
        self.__x=x0

    def random_int(self):
        self.__x = (self.__a * self.__x + self.__b)%(self.__m)
        return self.__x
    def random_float(self):
        self.__x = (self.__a * self.__x + self.__b)%(self.__m)
        return self.__x/self.__m


random1=random_lcd(1601,3456,10000, 0.9643972517176764
)
count=0
a1 = []
for i in range(10000):
    tmp = random1.random_float()
    a1.append(tmp)
    if tmp==0.5:
        count=count+1

print("Vorkommen bei passenden Startwert:")
print(count)
print("Passende Startwerte:")
for i in range(10):
    a=1601
    b=3456
    m=10000
    print((m*i+5000-b)/a)
