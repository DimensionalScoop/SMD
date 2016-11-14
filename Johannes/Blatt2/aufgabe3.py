import ROOT
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


## a)

def f(x_0, x_min, x_max, z):
    lenght = x_max-x_min
    my_array = []
    my_array.append(x_0)
    p = x_0
    for i in range(0,z-1):
        p = (137*p + 187) % (2**16)
        my_array.append(p)
    my_array = np.array(my_array)/(2**16)*lenght+x_min
    return my_array


canvas = ROOT.TCanvas("canvas", "Aufgabe 3a")
#canvas.Divide(3,2)

x = f(56536, 20, 25, 10000)
print(x)
canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall, bins=21", 21, min(x), max(x))
for tmp in x:
    h.Fill(tmp)
h.Draw()
#o = ROOT.TF1("f","f,1/2",1/2, 20, 25)
#o.Draw()
canvas.Print("3a.pdf")

## b)

def g(x_0, tau, z):
    return (-tau*np.log(f(x_0,0,1, z)*tau))
x = f(236234,0,10000000, 10000)
print(x)
x = g(236234, 10, 10000)
print(x)
canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall, bins=21", 21, 0, max(x))
for tmp in x:
    h.Fill(tmp)
h.Draw()

canvas.Print("3b.pdf")


## c)

def h(x_0, x_min, x_max, n, z):
    N = (-n+1)*1/(-x_min**(1-n)+x_max**(1-n))
    print(N)
    #print(f(x_0,N*x_min**(-n),N*x_max**(-n), z))
    return (np.exp(-np.log(f(x_0,N*x_max**(-n),N*x_min**(-n), z)/N)/n))

x = h(236234, 10, 20, 3, 10000)
print(x)
canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall, bins=21", 21, 10, 20)
for tmp in x:
    h.Fill(tmp)
h.Draw()

canvas.Print("3c.pdf")

## d)

def d(x_0, x_min, x_max, z):
    print(f(x_0,1/(np.pi*(1+x_max**2)),1/(np.pi*(1+x_min**2)), z))
    print(1/(np.pi*f(x_0,1/(np.pi*(1+x_max**2)),1/(np.pi*(1+x_min**2)), z))-1)
    return (np.sqrt(1/(np.pi*f(x_0,1/(np.pi*(1+x_max**2)),1/(np.pi*(1+x_min**2)), z))-1))

x = d(236234, 0.00001, 10000, 10000)
print(x)
canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall, bins=21", 21, 10, 20)
for tmp in x:
    h.Fill(tmp)
h.Draw()

canvas.Print("3d.pdf")


## e)

plt.clf()

data = np.load("empirisches_histogramm.npy")
plt.hist(data['bin_mid'], bins=np.linspace(0.,1.,50), weights=data['hist'])
print(data[0][0])
n = len(data)
m = []
for i in range(0,n-1):
    for l in range(0,int(data[i][1])):
        m.append(data[i][0])

print(m)


mu = np.mean(m)
sigma = np.std(m)

def Gauss(x, mu, sigma):
     return 1/(sigma*np.sqrt(2*np.pi) ) * np.exp(-0.5*  ((x-mu)/sigma)**2 )

#def poisson()


t_plot = np.linspace(0, 1, 10000)
plt.plot(t_plot, Gauss(t_plot, mu, sigma), 'r-', label='Gaußverteilung')


#plt.axis([40, 160, 0, 0.03])
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)





plt.savefig('3e.pdf')
