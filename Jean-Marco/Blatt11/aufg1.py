import numpy as np

def kolmo(size, lam, alpha):
    sigma = np.sqrt(lam)
    s1 = np.random.poisson(lam, size)
    s2 = np.rint(np.random.normal(lam, sigma, size)) # Zufallszahlen
    s1_hist = np.histogram(s1, bins=100, range=(lam-5*sigma, lam+5*sigma), density=True ) # Histogrammieren
    s2_hist = np.histogram(s2, bins=100, range=(lam-5*sigma, lam+5*sigma), density=True )
    s1_cum = np.cumsum(s1_hist[0]) # Kumullierte Summe
    s2_cum = np.cumsum(s2_hist[0])
    diff = np.abs(s1_cum - s2_cum)
    d_max = np.max(diff)
    test_val = np.sqrt(size**2 / (2*size) ) * d_max
    K_alpha = np.sqrt(np.log(2/alpha)/2)
    return( test_val<K_alpha)

for a in [0.05, 0.025, 0.001]:
    i = 1
    while i<=10000:
        val = kolmo(10000, i, a)
        if val==True:
            print("H0 wahr für a= ", a, "wahr ab Lambda = ", i)
            break
        i = i+1
