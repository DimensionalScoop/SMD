# Blatt 1
Gruppe *import antigravity*.  
Jean-Marco Alameddine, Johannes Kollek, Max Pernklau

## Aufgabe 1

Aufgabe *1* ist am Ende des Dokumentes (oder alternativ als PDF-Datei) als Scan eingebunden!


## Aufgabe 2
###a)
Der der der vorgegebenen Vorschrift programmierte LCG ist im Code programmiert und angegeben.

###b)
Die 10000 Zufallszahlen sind im vorliegenden Histogram dargestellt.
![10000 Zufallszahlen mit eigenen Zufallszahlengenerator](fig/2b_1.pdf)
Es fallen zwei Sachen auf, die den Anfordernungen an einen Zufallsgenerator widersprechen:
Zunächst ist eine starke Periodizität von Minima und Maxima der Bins zu erkennen. Zudem sind die Werte der Bins für jeden zweiten Bin identisch.
Dies widerspricht offensichtlich den Anspruch an einen Zufallsgenerator.
Die Periodizität der ausgegebenen Zahlen scheint deutlich zu gering zu sein, so dass bei der Erzeugung der 10000 Zufallszahlen mehrmals die selbe Zahlenfolge vom Generator ausgegeben wird.

Im Histogram scheint keine Abhängigkeit von $x_0$ vorhanden zu sein. Bei Betrachtung der Daten fällt jedoch auf, dass die einzelnen Zahlen sehr wohl einen Einfluss auf die ausgegebenen Zahlen haben: Die Zahlenwerte sind jeweils unterschiedlich. Keine Änderung kann jedoch in der ungewollten Periodizität der Daten gesehen werden.

###c)
Die Paare bzw. Triplets sind in den gegebenen Histogrammen dargestellt.
Man erkennt im Zweidimensionalen Histogram eindeutig ein periodisches Muster.
Dies zeigt direkt, dass der Generator nicht zufällig arbeitet und eine zu gerinige Periodizität der ausgegebenen Daten vorliegt.
Beim Dreidimensionalen Plot ergibt sich das gleiche Problem:
Hier äußert es sich darin, dass die Punkte im Raum jeweils auf Ebenen, hier 3, gruppiert sind.
Auch dies zeugt von einer Korreliertheit der Daten.

![Zweidimensionales Histogram mit eigenem Generator](2c_1.pdf)

![Dreidimensionales Histogram mit eigenem Generator](2c_2.pdf)

###d)
Bei dem in ROOT Implementierten Generator handelt es sich ebenfalls um einen linearen, konruenten Generator. Er funktioniert ähnlich zu dem angegebenen, jedoch sind die Startwerte sowie $a$ und $b$ so gewählt, dass eine möglichst hohe Periodizität von $2^{31}$ vorhanden ist.

###e)
Die verschiedenen Histogramme mit dem ROOT-Zufallszahlengenerator sind jeweils angegeben.

![Eindimensionales Histogram mit ROOT-Generator](fig/2e_1.pdf)

![Zweidimensionales Histogram mit ROOT-Generator](fig/2e_2.pdf)

![Dreidimensonales Histogram mit ROOT-Generator](fig/2e_4.pdf)

Man erkennt sofort die verbesserte Periodizität:
Es gibt keine Muster in den zweidimensionales Histogrammen und keine Ansammlung von Ebenen im dreidimensionalen Scatter-Plot!

###f)
Bei eigenen Generator kommt der exkate Wert von $0.5$ bei zufälligen Startwerten gar nicht vor. Dies wurde für mehrere Eingabewerte überprüft.
Um die Ausgabe einer exakten 0.5 zu erzwingen, kann die Erzeugungsvorschrift zu $x_n$ umgestellt weden, so dass der erste ausgegebene Wert direkt 0.5 ist.
Die möglichen Startwerte nach dieser Berechnung werden vom Python Script ausgegeben.
Man erhält dabei jedoch nicht nur ein mal den Wert 0.5 sondern gleich mehrfach (bei uns 16 mal). Grund dafür ist die bereits angesprochene stark begrenze Periodizität!

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

![Die Turm-zur-Babel-Methode](fig/3e3.pdf)

![Das gegebene Histogramm](fig/3e-orginale-daten.pdf)


## Aufgabe 4

Teilaufgabe *4a)* ist am Ende des Dokumentes (oder alternativ als PDF-Datei) als Scan eingebunden!

Im Scatterplot ist deutlich die Korrelation der beiden Normalverteilungen zu sehen. Es wurden 10000 Wertepaare generiert.

Die Abweichung schwanken zufällig, da die nicht besonders viele Wertpaare generiert wurden. Der grobe Kurvenverlauf bleibt aber ähnlich, die Anzahl der Peaks und ihre Position verändern sich jedoch.


  x  Analytical Nom  Analytical Std  Monte Carlo Nom  Monte Carlo Std  
---- --------------  --------------  ---------------  ---------------  
 3.0            4.0         0.45607         3.996402         0.456447    
 0.0            1.0             0.2          1.00488         0.198824    
-3.0           -2.0        0.769415        -1.986642         0.76789   

: Ausgesuchte Werte der Simulation und Analytik.



  x  Relative Difference Nom  Relative Difference Std
---- -----------------------  -----------------------
 3.0  0.0009                    0.000827   
 0.0  0.00488                   0.005882  
-3.0 -0.006679                 0.001983

: Vergleich der Abweichungen Abweichungen


![Scatterplot der Parameter $a_0$ und $a_1$](fig/4b-a.pdf)

![Betrag der relativen Abweichung der analytischen von den simulierten Werte.](fig/4b-diff.pdf)

## Anhang

![Scatterplot der Parameter $a_0$ und $a_1$](Aufg1+4a.pdf)
