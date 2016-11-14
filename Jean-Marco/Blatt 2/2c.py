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
        self.__x = (self.__a * self.__x + self.__b) % (self.__m)
        return self.__x
    def random_float(self):
        self.__x = (self.__a * self.__x + self.__b) % (self.__m)
        return self.__x/self.__m

random1=random_lcd(1601,3456,10000,0)

#2d

a1 = []
a2= []
for i in range(5000):
    a1.append(random1.random_float())
    a2.append(random1.random_float())

plt.hist2d(a1, a2, bins=50)
plt.colorbar()
plt.title("5000 Zufallstupel als Histogram - 50 Bins")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('2c_1.pdf')

plt.clf()

#3d

b1=[]
b2=[]
b3=[]
for i in range(3000):
    b1.append(random1.random_float())
    b2.append(random1.random_float())
    b3.append(random1.random_float())


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.view_init(14,39)
ax.scatter(b1, b2, b3, lw=0, s=5, c='r')
plt.title("3000 Zufalltripel")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.savefig('2c_2.pdf')

plt.clf()
