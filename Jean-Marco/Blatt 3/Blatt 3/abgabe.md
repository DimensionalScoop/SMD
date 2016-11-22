# Blatt3

##Aufgabe1

### a)

Der Normierungsfaktor wird auf
\begin{align*}
  \Phi_0 = \gamma-1
\end{align*}
bestimmt. Über die Methode des letzten Blattes,
\begin{align*}
  F = \int^x_1 \Phi_0 E^{-\gamma} \mathrm{d}E = 1 - x^{1 - \gamma}
\end{align*}
nach x umstellen, wobei F eine gleichverteilte Zufallszahl im Intervall [0,1] ist, wird die Energieverteilung der Neutrions ermittelt.
Die sich ergebene Transformationsformel ist somit
\begin{align*}
  E(r) = (1-r)^\frac{1}{1-\gamma}.
\end{align*}
Die Energien werden in TeV ausgegeben bzw in *NeutrinoMC.root* abgespeichert.
Es folgt ein Beispielhistogramm, welches die Neutrionenergien angibt.

![Beispielhistogramm zu a)](fig/1a.pdf)

### b)

Die Energien von a) werden durch die Wahrscheinlichkeit über das *Neumann'sche Rückweisungsverfahren* nach der gegebenen Wahrscheinlichkeitsfunktion gefiltert und in einem neuen Branch gespeichert.
Die Ergebnisse sind in den folgenden Plots dargestellt.

![Tatsächlich detektierte Ergebnisse](fig/1b.pdf)
![Tatsächlich detektierte Ergebnisse und Ergebnisse im Vergleich](fig/1b2.pdf)

### c)

Für jede akzeptierte Energie $E$ wird über die Polarmethode, bei gegebenen $\mu=10 \cdot E$ und $\sigma=2 \cdot E$, eine normalverteilte auf eine ganze Zahl gerundete Zufallszahl, welche größer als Null ist, generiert.
Diese steht für die Anzahl der Hits $N$.
Die Ergebnisse werden in einem Branch abgespeichert und sind zusätzlich in unterer Abbildung illustriert.

![Anzahl der auftretenen Hits in einem Histogram](fig/1c.pdf)

### d)

Es soll ein Ort für das Auftreffen der Neutrinos ermittelt werden:
Zur gegebenen Anzahl der Hits wird jeweils eine normalverteilte x- und y-Koordinate erstellt, deren Mittelwert bei $(7,3)$ liegt und deren Standardabweichung aus der Hitzahl berechnet wird (unkorreliert).
Koordinaten, welche nicht in den Detektor fallen, werden solange ersetzt bis ein passender Punkt generiert wird.
Die Ergebnisse werden abgespeichert und sind in folgender Heatmap dargestellt.

![Hits in Abhängigkeit des Ortes](fig/1d_hist.pdf)

### e)

Zunächst wird die Anzahl der Hits generiert.
Dafür werden zunächt positive normalverteilte Zufallszahlen erzeugt.
Die Anzahl der Hits entspricht dann der auf eine ganze Zahl gerundeten Zehnerpotenz der Zufallszahl.
Die Ergebnisse sind in folgendem Histogramm dargestellt.

![Häufigkeit der Hits](fig/1e_hits.pdf)

Um die Ortsmessung zu realisieren, werden normalverteilte Koordinaten über die Formel des Blattes modifiziert.
Zusätzlich werden nur die akzeptiert, welche in den Detektor fallen.
Diese Heatmap ist hier dargestellt.

![Korrelierte Hits in Abhängigkeit des Ortes](fig/1e_hist.pdf)

In *fig* Ordner sind weitere, der Aufgabe entsprechende Histogramme zu finden.
