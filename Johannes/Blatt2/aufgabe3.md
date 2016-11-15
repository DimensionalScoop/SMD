## Aufgabe 3

###a)

Für diese Aufgabe wird der Zufallsgenerator von ROOT, welcher eine Zufallszahl im Intervall [0,1] ausgibt, auf die gewünschte Länge des gewünschten Zufallsintervalls skaliert und mit der unteren Grenze des Intervalls summiert. Das Ergebnis ist in unterer Abbildung exemplarisch für ein Intervall dargestellt.

![Gleichverteilt generierte Zufallszahlen](fig/3a.pdf)

###b)

Gegeben ist die Verteilungsfunktion

\begin{align*}
  f(t) = N e^{-\frac{t}{\tau}}
\end{align*}

Dabei ist die Normierungskonstante $N = \frac{1}{\tau}$. Um Zufallszahlen gegebener Verteilung zu generieren, wird zunächst die Funktion von $x_{\text{min}}$ bis $x$ integriert,

\begin{align*}
  \int_0^x N e^{-\frac{t}{\tau}} \mathrm{d}t = -(e^{-\frac{x}{\tau}}-1) = u.
\end{align*}

Aufgelöst nach $x$ ergibt die neue Zufallszahl

\begin{align*}
  x = -\tau \ln(1-u).
\end{align*}

Dabei beschreibt u eine nach *a)* gleichverteilte Zufallszahl von 0 bis 1. Es folgt ein Beispielplot.

![Exponentialverteilte Zufallszahlen](fig/3b.pdf)

###c)

Hier wird verfahren wie in Aufgabenteil *b)*, wobei die Normierungskonsante

\begin{align*}
  N = \frac{1-n}{(x_{\text{max}})^{1-n}-(x_{\text{min}})^{1-n}}
\end{align*}
beträgt. Anbei ein Beispiel.

![Nach dem Potenzgesetz verteilte Zufallszahlen](fig/3c.pdf)

###d)

Gleiches Vorgehen wie zuvor führt auf den Beispielplot:

![Cauchy-verteilte Zufallszahlen](fig/3d.pdf)


###e)

Zum Anpassen der Zufallszahlen an die gegebene diskrete Verteilung wird folgendermaßen vorgegangen:
Zunächst wird die Gesamtzahl der Histogrammeinträge summiert.
Es werden gleichverteilt Zufallszahlen von 0 bis der Gesamtzahl der Einträge generiert.
Bildlich gesprochen werden alle Bins der Höhe nach aufeinander gestapelt.
Dann wird der Bin gesucht in den die Zufallszahl trifft.
Als nächstes wird diese Zahl so verrechnet bzw skaliert, dass sie eine Zahl im Bereich der Binbreite eben des Bins entspricht, auf welchen sie zuvor gefallen ist.
Daraus ergibt sich folgende Verteilung (darunter der Vergleich zum gegebenen Histogramm).

![Die Turm-zur-Babel-Methode](fig/3e2.pdf)

![Das gegebene Histogramm](fig/3e_1.pdf)
