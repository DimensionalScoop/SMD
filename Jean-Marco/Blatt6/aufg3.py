import numpy as np
import matplotlib.pyplot as plt

def I(p,n):
    if p==0 or n==0:
        return 0
    return -p/(p+n)*np.log2(p/(p+n)) - n/(p+n) * np.log2(n/(p+n))

#Daten
temp = np.array([29.4, 26.7, 28.3, 21.1, 20, 18.3, 17.8, 22.2, 20.6, 23.9, 23.9, 22.2, 27.2, 21.7])
foot = np.array([False, False, True, True, True, False, True, False, True, True, True, True, True, False])
moist = np.array([85, 90, 78, 96, 80, 70, 65, 95, 70, 80, 70, 90, 75, 80])
forec = np.array([2,2,1,0,0,0,1,2,2,0,2,1,1,0])
wind = np.array([False, True, False, False, False, True, True, False, False, False, True, True, False, True])

def gain(a, label, cutdata):
    '''Returns the gain of information. a is the parameter where to cut the array. label is the array that classifies the elements (True/False). cutdata is the attribute that giving the cut '''
    l_part = cutdata<a # cut data into two parts
    r_part = cutdata>=a
    p = sum(label) # p = how many values are labled true (positive)
    n = sum(~label)
    p_left = sum(label[l_part]) # how many values labled true are in the left part
    n_left = sum(~label[l_part])
    p_right = sum(label[r_part])
    n_right = sum(~label[r_part])
    E = (p_left + n_left)/(p+n) * I(p_left, n_left) + (p_right + n_right)/(p+n) * I(p_right, n_right)
    return I(p,n) - E

#Test stuff
print("Informationsgewinne:")
print("Schnitt im Wind (vgl. Handrechnung):", gain(True, foot, wind))
print("Schnitt in Wettervorhersage in (0,1) und (2):", gain(1, foot, forec))
print("Schnitt in Wettervorhersage in (0) und (1,2):", gain(2, foot, forec))

plot_temp = np.linspace(17,30,131)
plot_temp_val = []
for i in plot_temp:
    plot_temp_val.append(gain(i, foot, temp))
plt.plot(plot_temp, plot_temp_val)
plt.xlabel(r'$T_{cut} \ K$')
plt.ylabel('Gain')
plt.savefig('1_temp.pdf')
plt.clf()

plot_moist = np.linspace(60,100,41)
plot_moist_val = []
for i in plot_moist:
    plot_moist_val.append(gain(i, foot, moist))
plt.plot(plot_moist, plot_moist_val)
plt.xlabel(r'$f_{cut} \ %$')
plt.ylabel('Gain')
plt.savefig('1_moist.pdf')
